"""
Initiative generator for all three team types.
"""

from datetime import datetime
import logging

import config

logger = logging.getLogger(__name__)


class InitiativeGenerator:
    """Generates initiative data for all teams."""
    
    # Product Development Initiatives
    PD_INITIATIVES = [
        ("pd_init_1", "team_pd", "Core Platform Modernization", "platform",
         "Upgrade core systems for scale and reliability", "2025-07-01", "2025-12-31", "active"),
        ("pd_init_2", "team_pd", "New Feature Delivery – Q1", "feature",
         "Deliver high-impact customer features", "2025-07-15", "2025-10-15", "active"),
        ("pd_init_3", "team_pd", "Mobile App Revamp", "feature",
         "Improve mobile UX and performance", "2025-08-01", "2025-11-30", "planned"),
        ("pd_init_4", "team_pd", "Backend Scalability Upgrade", "infra",
         "Handle 10x traffic growth", "2025-07-10", "2026-01-10", "active"),
        ("pd_init_5", "team_pd", "API & Integration Expansion", "platform",
         "Enable third-party ecosystem", "2025-09-01", "2025-12-31", "planned"),
        ("pd_init_6", "team_pd", "Security & Compliance Program", "security",
         "Meet enterprise compliance standards", "2025-07-01", "2025-12-31", "active"),
        ("pd_init_7", "team_pd", "Developer Experience Improvement", "feature",
         "Reduce build and deployment friction", "2025-08-01", "2025-11-15", "planned"),
    ]
    
    # Marketing Initiatives
    MKT_INITIATIVES = [
        ("mkt_init_1", "team_mkt", "Brand Awareness Campaign", "branding",
         "Increase brand visibility across channels", "2025-07-01", "2025-12-31", "active"),
        ("mkt_init_2", "team_mkt", "Product Launch Marketing", "launch",
         "Support major product launches", "2025-07-15", "2025-10-15", "active"),
        ("mkt_init_3", "team_mkt", "Growth Marketing Program", "growth",
         "Drive acquisition and activation", "2025-08-01", "2025-12-31", "active"),
        ("mkt_init_4", "team_mkt", "Content Marketing Engine", "content",
         "Scale high-quality content output", "2025-07-10", "2025-11-30", "planned"),
        ("mkt_init_5", "team_mkt", "Performance Marketing", "performance",
         "Optimize paid marketing ROI", "2025-07-01", "2025-12-31", "active"),
        ("mkt_init_6", "team_mkt", "Customer Retention Program", "retention",
         "Improve engagement and reduce churn", "2025-08-01", "2025-12-31", "active"),
        ("mkt_init_7", "team_mkt", "Marketing Operations", "operations",
         "Improve marketing systems and processes", "2025-07-01", "2025-12-31", "active"),
    ]
    
    # Operations Initiatives
    OPS_INITIATIVES = [
        ("ops_init_1", "team_ops", "Business Process Optimization", "process",
         "Improve internal workflows and efficiency", "2025-07-01", "2025-12-31", "active"),
        ("ops_init_2", "team_ops", "Customer Support Operations", "customer_support",
         "Scale and improve customer support quality", "2025-07-01", "2025-12-31", "active"),
        ("ops_init_3", "team_ops", "Finance & Billing Operations", "finance",
         "Ensure accurate billing and payments", "2025-07-15", "2025-12-31", "active"),
        ("ops_init_4", "team_ops", "Risk & Compliance Operations", "compliance",
         "Meet regulatory and audit requirements", "2025-08-01", "2025-12-31", "active"),
        ("ops_init_5", "team_ops", "Internal Infrastructure Operations", "infrastructure",
         "Maintain internal systems and tools", "2025-07-01", "2025-12-31", "active"),
        ("ops_init_6", "team_ops", "Vendor & Partner Management", "vendor",
         "Manage external vendors and partners", "2025-07-01", "2025-12-31", "active"),
    ]
    
    def __init__(self, db_manager):
        self.db = db_manager
    
    def generate(self):
        """Generate all initiative records."""
        # Product Development Initiatives
        for init in self.PD_INITIATIVES:
            self.db.insert_one("product_development_initiatives", {
                "initiative_id": init[0],
                "team_id": init[1],
                "initiative_name": init[2],
                "initiative_type": init[3],
                "objective": init[4],
                "employee_capacity": 500,
                "start_date": init[5],
                "end_date": init[6],
                "status": init[7],
                "created_at": datetime.now().isoformat()
            })
        logger.info(f"Created {len(self.PD_INITIATIVES)} product development initiatives")
        
        # Marketing Initiatives
        for init in self.MKT_INITIATIVES:
            self.db.insert_one("marketing_initiatives", {
                "initiative_id": init[0],
                "team_id": init[1],
                "initiative_name": init[2],
                "initiative_type": init[3],
                "objective": init[4],
                "employee_capacity": 500,
                "start_date": init[5],
                "end_date": init[6],
                "status": init[7],
                "created_at": datetime.now().isoformat()
            })
        logger.info(f"Created {len(self.MKT_INITIATIVES)} marketing initiatives")
        
        # Operations Initiatives
        for init in self.OPS_INITIATIVES:
            self.db.insert_one("operation_flow_initiatives", {
                "initiative_id": init[0],
                "team_id": init[1],
                "initiative_name": init[2],
                "initiative_type": init[3],
                "objective": init[4],
                "employee_capacity": 500,
                "start_date": init[5],
                "end_date": init[6],
                "status": init[7],
                "created_at": datetime.now().isoformat()
            })
        logger.info(f"Created {len(self.OPS_INITIATIVES)} operation initiatives")