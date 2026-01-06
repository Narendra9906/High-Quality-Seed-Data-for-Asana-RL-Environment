"""
Organization generator.
"""

import uuid
from datetime import datetime
import logging

import config

logger = logging.getLogger(__name__)


class OrganizationGenerator:
    """Generates organization data."""
    
    def __init__(self, db_manager):
        self.db = db_manager
    
    def generate(self):
        """Generate the organization record."""
        org = config.ORGANIZATION
        
        self.db.insert_one("organizations", {
            "organization_id": org["id"],
            "name": org["name"],
            "domain": org["domain"],
            "created_at": datetime.now().isoformat()
        })
        
        logger.info(f"Created organization: {org['name']}")