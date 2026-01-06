from dataclasses import dataclass
from datetime import date, datetime
from typing import Optional

@dataclass
class Project:
    project_id: str
    team_id: str
    owner_id: str
    name: str
    description: str
    status: str
    due_date: date
    created_at: datetime
    workstream_id: Optional[str] = None # Linking to your Strategy layer
    archived: bool = False