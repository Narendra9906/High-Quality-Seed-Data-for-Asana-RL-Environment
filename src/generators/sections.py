import uuid
from datetime import datetime

class SectionGenerator:
    def __init__(self, conn):
        self.conn = conn

    def create_sections_for_project(self, project_id, project_type):
        """Creates standard Asana sections based on project type."""
        cursor = self.conn.cursor()
        
        if project_type == 'engineering':
            names = ["Backlog", "To Do", "In Progress", "Code Review", "Testing", "Done"]
        elif project_type == 'marketing':
            names = ["Briefing", "Asset Creation", "Review", "Publishing", "Distribution"]
        else:
            names = ["New Requests", "In Progress", "Blocked", "Completed"]

        sections_data = []
        section_ids = []
        
        for name in names:
            sec_id = str(uuid.uuid4())
            sections_data.append((sec_id, project_id, name, datetime.now()))
            section_ids.append(sec_id)

        cursor.executemany("INSERT INTO sections (section_id, project_id, name, created_at) VALUES (?, ?, ?, ?)", sections_data)
        return section_ids # Return IDs so we can add tasks to them later