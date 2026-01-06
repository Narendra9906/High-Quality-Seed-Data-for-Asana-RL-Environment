from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Task:
    task_id: str
    project_id: str
    name: str
    created_at: datetime
    section_id: Optional[str] = None
    assignee_id: Optional[str] = None
    description: Optional[str] = ""
    priority: str = "medium"
    due_date: Optional[date] = None
    completed: bool = False
    completed_at: Optional[datetime] = None