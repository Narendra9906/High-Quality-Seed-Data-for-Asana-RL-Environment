from dataclasses import dataclass
from datetime import datetime

@dataclass
class Team:
    team_id: str
    organization_id: str
    name: str
    team_type: str
    employee_count: int
    created_at: datetime