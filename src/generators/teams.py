"""
Team generator.
"""

from datetime import datetime
import logging

import config

logger = logging.getLogger(__name__)


class TeamGenerator:
    """Generates team data."""
    
    def __init__(self, db_manager):
        self.db = db_manager
    
    def generate(self):
        """Generate team records."""
        for team in config.TEAMS:
            self.db.insert_one("teams", {
                "team_id": team["id"],
                "organization_id": config.ORGANIZATION["id"],
                "name": team["name"],
                "team_type": team["type"],
                "employee_count": team["employee_count"],
                "created_at": datetime.now().isoformat()
            })
            logger.info(f"Created team: {team['name']}")