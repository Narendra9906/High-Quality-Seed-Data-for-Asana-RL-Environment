import uuid
import random
from datetime import datetime
from utils.db_utils import get_db_connection
from generators.sections import SectionGenerator
from config import NUM_PROJECTS

class ProjectGenerator:
    def __init__(self):
        self.conn = get_db_connection()
        self.section_gen = SectionGenerator(self.conn)
        
        # Mapping your custom schema tables to Project Types
        self.strategy_tables = [
            ('pd_core_platform_workstreams', 'engineering', 'team_pd'),
            ('pd_feature_delivery_workstreams', 'engineering', 'team_pd'),
            ('mkt_brand_awareness_workstreams', 'marketing', 'team_mkt'),
            ('ops_process_optimization_workstreams', 'operations', 'team_ops')
            # Add other tables from your schema here
        ]

    def generate(self):
        cursor = self.conn.cursor()
        projects_created = 0
        
        # Get potential owners
        cursor.execute("SELECT user_id, department FROM users")
        users = cursor.fetchall()
        
        print(f"Generating Projects from Strategy Workstreams...")

        for table_name, proj_type, team_id in self.strategy_tables:
            # 1. Fetch workstreams from your custom strategy tables
            # We use try/except in case a specific table wasn't created in schema
            try:
                cursor.execute(f"SELECT workstream_id, workstream_name, status, lead_role FROM {table_name}")
                workstreams = cursor.fetchall()
            except Exception as e:
                print(f"Skipping {table_name}: {e}")
                continue

            for ws in workstreams:
                if projects_created >= NUM_PROJECTS:
                    break

                # Find a suitable owner
                dept_users = [u for u in users if u['department'] == ('product' if proj_type == 'engineering' else proj_type)]
                owner = random.choice(dept_users)['user_id'] if dept_users else None

                project_id = str(uuid.uuid4())
                
                # Insert Project linked to Workstream
                cursor.execute("""
                    INSERT INTO projects (project_id, workstream_id, team_id, owner_id, name, description, status, created_at)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
                """, (
                    project_id,
                    ws['workstream_id'], # THE LINK
                    team_id,
                    owner,
                    ws['workstream_name'], # Project Name = Workstream Name
                    f"Execution project for {ws['workstream_name']} ({ws['lead_role']})",
                    'on_track' if ws['status'] == 'active' else 'on_hold',
                    datetime.now()
                ))
                
                # Create Sections for this project
                self.section_gen.create_sections_for_project(project_id, proj_type)
                
                projects_created += 1

        self.conn.commit()
        print(f"Generated {projects_created} projects linked to strategy.")