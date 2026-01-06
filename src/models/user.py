from dataclasses import dataclass
from datetime import datetime

@dataclass
class User:
    user_id: str
    organization_id: str
    email: str
    full_name: str
    job_title: str
    department: str
    created_at: datetime
    avatar_url: str = None