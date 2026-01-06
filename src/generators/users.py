import uuid
import random
from datetime import timedelta
from utils.db_utils import get_db_connection
from utils.name_generator import NameGenerator
from utils.date_utils import get_random_date
from config import NUM_USERS, DOMAIN

class UserGenerator:
    def __init__(self):
        self.conn = get_db_connection()
        self.name_gen = NameGenerator()
        
    def generate(self):
        cursor = self.conn.cursor()
        
        # 1. Fetch Teams from DB to assign users correctly
        cursor.execute("SELECT team_id, name, team_type FROM teams")
        teams = cursor.fetchall()
        
        if not teams:
            print("No teams found. Run schema setup first.")
            return

        users_data = []
        print(f"Generating {NUM_USERS} users...")

        for _ in range(NUM_USERS):
            user_id = str(uuid.uuid4())
            full_name = self.name_gen.generate_full_name()
            first, last = full_name.split(" ", 1)
            email = f"{first.lower()}.{last.lower()}@{DOMAIN}"
            
            # Weighted Random Team Assignment
            # 50% Product, 10% Marketing, 40% Ops
            weights = [0.5 if t['team_type'] == 'product' else 0.1 if t['team_type'] == 'marketing' else 0.4 for t in teams]
            team = random.choices(teams, weights=weights, k=1)[0]
            
            job_titles = {
                'product': ['Software Engineer', 'Product Manager', 'Designer', 'QA Engineer'],
                'marketing': ['Marketing Specialist', 'Content Writer', 'SEO Analyst'],
                'operations': ['Ops Analyst', 'Customer Support', 'Finance Associate']
            }
            title = random.choice(job_titles.get(team['team_type'], ['Employee']))
            
            joined_at = get_random_date("2024-01-01", "2025-01-01")

            users_data.append((
                user_id, 'org_1', email, full_name, title, team['team_type'], joined_at
            ))

        # Bulk Insert
        cursor.executemany("""
            INSERT INTO users (user_id, organization_id, email, full_name, job_title, department, created_at)
            VALUES (?, ?, ?, ?, ?, ?, ?)
        """, users_data)
        
        self.conn.commit()
        print("Users generated successfully.")