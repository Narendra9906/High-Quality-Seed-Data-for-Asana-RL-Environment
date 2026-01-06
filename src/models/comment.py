from dataclasses import dataclass
from datetime import datetime

@dataclass
class Comment:
    comment_id: str
    task_id: str
    user_id: str
    text_content: str
    created_at: datetime