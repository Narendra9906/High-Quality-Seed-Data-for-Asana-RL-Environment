import uuid
import random
from datetime import datetime
from utils.db_utils import get_db_connection
from utils.llm_utils import ContentGenerator

class CommentGenerator:
    def __init__(self):
        self.conn = get_db_connection()
        self.llm = ContentGenerator()

    def generate(self):
        cursor = self.conn.cursor()
        print("Generating Comments...")

        cursor.execute("SELECT task_id, assignee_id, created_at FROM tasks LIMIT 1000")
        tasks = cursor.fetchall()

        comments_data = []
        
        for task in tasks:
            if random.random() > 0.7: # 30% chance of comment
                comment_id = str(uuid.uuid4())
                text = self.llm.generate_text("comments", {'context': 'update'})
                
                comments_data.append((
                    comment_id,
                    task['task_id'],
                    task['assignee_id'], # Assigned user comments
                    text,
                    datetime.now()
                ))

        cursor.executemany("""
            INSERT INTO comments (comment_id, task_id, user_id, text_content, created_at)
            VALUES (?, ?, ?, ?, ?)
        """, comments_data)
        
        self.conn.commit()
        print(f"Generated {len(comments_data)} comments.")