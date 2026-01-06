import uuid
import random
from datetime import timedelta
from utils.db_utils import get_db_connection
from utils.llm_utils import ContentGenerator
from utils.date_utils import get_random_date
from config import AVG_TASKS_PER_PROJECT

class TaskGenerator:
    def __init__(self):
        self.conn = get_db_connection()
        self.llm = ContentGenerator()

    def generate(self):
        cursor = self.conn.cursor()
        print("Generating Tasks (this may take a moment)...")

        # 1. Get all projects with their details
        cursor.execute("""
            SELECT p.project_id, p.name, p.team_id, t.team_type, p.created_at
            FROM projects p
            JOIN teams t ON p.team_id = t.team_id
        """)
        projects = cursor.fetchall()

        tasks_data = []
        
        for project in projects:
            # Get sections for this project to distribute tasks
            cursor.execute("SELECT section_id FROM sections WHERE project_id = ?", (project['project_id'],))
            sections = [row['section_id'] for row in cursor.fetchall()]
            
            if not sections: continue

            # Get potential assignees (users in the same team)
            cursor.execute("""
                SELECT user_id FROM users 
                WHERE department = ? OR department = 'product'
            """, (project['team_type'],))
            team_users = [row['user_id'] for row in cursor.fetchall()]

            # Determine Prompt Template based on Team Type
            prompt_file = f"tasks_{project['team_type']}" if project['team_type'] in ['engineering', 'marketing'] else "tasks_operations"
            
            # Generate Raw Task Names (Simulation: requesting 5-10 tasks at once to save "calls")
            # In a real LLM scenario, we'd read the file content here. 
            # For the demo, the fallback in llm_utils handles the logic.
            
            num_tasks = random.randint(5, AVG_TASKS_PER_PROJECT)
            
            for _ in range(num_tasks):
                task_id = str(uuid.uuid4())
                
                # Generate Name
                task_name = self.llm.generate_text(prompt_file, {'project_name': project['name']})
                
                # Generate Description
                desc = self.llm.generate_text("task_descriptions", {'task_name': task_name})
                
                # Dates
                created_at = project['created_at'] # Simplified: Task created same time as project
                due_date = get_random_date(str(created_at)[:10], "2026-01-01")
                
                # Status Logic
                completed = random.choice([True, False])
                completed_at = str(get_random_date(str(created_at)[:10], str(due_date))) if completed else None

                tasks_data.append((
                    task_id,
                    project['project_id'],
                    random.choice(sections), # Random section
                    random.choice(team_users) if team_users else None,
                    task_name,
                    desc,
                    random.choice(['low', 'medium', 'high']),
                    due_date,
                    completed,
                    completed_at,
                    created_at
                ))

        # Batch Insert
        cursor.executemany("""
            INSERT INTO tasks (task_id, project_id, section_id, assignee_id, name, description, priority, due_date, completed, completed_at, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, tasks_data)
        
        self.conn.commit()
        print(f"Generated {len(tasks_data)} tasks across {len(projects)} projects.")