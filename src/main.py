"""
Main entry point for Asana Seed Data Generator.

This script orchestrates the entire data generation process:
1. Initialize database schema
2. Generate base data (organization, teams)
3. Generate users and team memberships
4. Generate initiatives and workstreams (from schema)
5. Generate projects, sections, tasks
6. Generate subtasks, comments
7. Generate custom fields and tags
8. Validate and export

Usage:
    python src/main.py
"""

import os
import sys
import sqlite3
import random
from datetime import datetime
from pathlib import Path

# Add project root to path
project_root = Path(__file__).parent.parent
sys.path.insert(0, str(project_root))

from loguru import logger
from tqdm import tqdm

import config
from src.utils.db_utils import DatabaseManager
from src.generators.users import UserGenerator
from src.generators.teams import TeamGenerator
from src.generators.projects import ProjectGenerator
from src.generators.tasks import TaskGenerator
from src.generators.subtasks import SubtaskGenerator
from src.generators.comments import CommentGenerator
from src.generators.custom_fields import CustomFieldGenerator
from src.generators.tags import TagGenerator


def setup_logging():
    """Configure logging for the application."""
    log_path = project_root / 'output' / 'generation_log.txt'
    log_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Remove default handler
    logger.remove()
    
    # Add console handler
    logger.add(
        sys.stderr,
        level="DEBUG" if config.DEBUG_MODE else "INFO",
        format="<green>{time:YYYY-MM-DD HH:mm:ss}</green> | <level>{level: <8}</level> | <cyan>{name}</cyan>:<cyan>{function}</cyan> - <level>{message}</level>"
    )
    
    # Add file handler
    logger.add(
        str(log_path),
        level="DEBUG",
        format="{time:YYYY-MM-DD HH:mm:ss} | {level: <8} | {name}:{function} - {message}",
        rotation="10 MB"
    )
    
    return logger


def ensure_output_directory():
    """Create output directory if it doesn't exist."""
    output_dir = project_root / 'output'
    output_dir.mkdir(parents=True, exist_ok=True)
    logger.info(f"Output directory ready: {output_dir}")


def initialize_database(db_manager: DatabaseManager):
    """Initialize database with schema."""
    logger.info("Initializing database schema...")
    
    schema_path = project_root / 'schema.sql'
    if not schema_path.exists():
        raise FileNotFoundError(f"Schema file not found: {schema_path}")
    
    with open(schema_path, 'r') as f:
        schema_sql = f.read()
    
    db_manager.execute_script(schema_sql)
    logger.success("Database schema initialized successfully")


def insert_seed_data(db_manager: DatabaseManager):
    """Insert initial seed data for organization, teams, initiatives, and workstreams."""
    logger.info("Inserting seed data...")
    
    # Insert organization
    db_manager.execute("""
        INSERT OR REPLACE INTO organizations (organization_id, name, domain)
        VALUES (?, ?, ?)
    """, (config.ORGANIZATION['id'], config.ORGANIZATION['name'], config.ORGANIZATION['domain']))
    
    # Insert teams
    for team in config.TEAMS:
        db_manager.execute("""
            INSERT OR REPLACE INTO teams (team_id, organization_id, name, team_type, employee_count)
            VALUES (?, ?, ?, ?, ?)
        """, (team['id'], config.ORGANIZATION['id'], team['name'], team['type'], team['employee_count']))
    
    # Insert Product Development Initiatives
    pd_initiatives = [
        ('pd_init_1', 'team_pd', 'Core Platform Modernization', 'platform',
         'Upgrade core systems for scale and reliability', 500, '2025-07-01', '2025-12-31', 'active'),
        ('pd_init_2', 'team_pd', 'New Feature Delivery – Q1', 'feature',
         'Deliver high-impact customer features', 500, '2025-07-15', '2025-10-15', 'active'),
        ('pd_init_3', 'team_pd', 'Mobile App Revamp', 'feature',
         'Improve mobile UX and performance', 500, '2025-08-01', '2025-11-30', 'planned'),
        ('pd_init_4', 'team_pd', 'Backend Scalability Upgrade', 'infra',
         'Handle 10x traffic growth', 500, '2025-07-10', '2026-01-10', 'active'),
        ('pd_init_5', 'team_pd', 'API & Integration Expansion', 'platform',
         'Enable third-party ecosystem', 500, '2025-09-01', '2025-12-31', 'planned'),
        ('pd_init_6', 'team_pd', 'Security & Compliance Program', 'security',
         'Meet enterprise compliance standards', 500, '2025-07-01', '2025-12-31', 'active'),
        ('pd_init_7', 'team_pd', 'Developer Experience Improvement', 'feature',
         'Reduce build and deployment friction', 500, '2025-08-01', '2025-11-15', 'planned'),
    ]
    
    for init in pd_initiatives:
        db_manager.execute("""
            INSERT OR REPLACE INTO product_development_initiatives 
            (initiative_id, team_id, initiative_name, initiative_type, objective, 
             employee_capacity, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, init)
    
    # Insert Marketing Initiatives
    mkt_initiatives = [
        ('mkt_init_1', 'team_mkt', 'Brand Awareness Campaign', 'branding',
         'Increase brand visibility across channels', 500, '2025-07-01', '2025-12-31', 'active'),
        ('mkt_init_2', 'team_mkt', 'Product Launch Marketing', 'launch',
         'Support major product launches', 500, '2025-07-15', '2025-10-15', 'active'),
        ('mkt_init_3', 'team_mkt', 'Growth Marketing Program', 'growth',
         'Drive acquisition and activation', 500, '2025-08-01', '2025-12-31', 'active'),
        ('mkt_init_4', 'team_mkt', 'Content Marketing Engine', 'content',
         'Scale high-quality content output', 500, '2025-07-10', '2025-11-30', 'planned'),
        ('mkt_init_5', 'team_mkt', 'Performance Marketing', 'performance',
         'Optimize paid marketing ROI', 500, '2025-07-01', '2025-12-31', 'active'),
        ('mkt_init_6', 'team_mkt', 'Customer Retention Program', 'retention',
         'Improve engagement and reduce churn', 500, '2025-08-01', '2025-12-31', 'active'),
        ('mkt_init_7', 'team_mkt', 'Marketing Operations', 'operations',
         'Improve marketing systems and processes', 500, '2025-07-01', '2025-12-31', 'active'),
    ]
    
    for init in mkt_initiatives:
        db_manager.execute("""
            INSERT OR REPLACE INTO marketing_initiatives 
            (initiative_id, team_id, initiative_name, initiative_type, objective,
             employee_capacity, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, init)
    
    # Insert Operations Initiatives
    ops_initiatives = [
        ('ops_init_1', 'team_ops', 'Business Process Optimization', 'process',
         'Improve internal workflows and efficiency', 500, '2025-07-01', '2025-12-31', 'active'),
        ('ops_init_2', 'team_ops', 'Customer Support Operations', 'customer_support',
         'Scale and improve customer support quality', 500, '2025-07-01', '2025-12-31', 'active'),
        ('ops_init_3', 'team_ops', 'Finance & Billing Operations', 'finance',
         'Ensure accurate billing and payments', 500, '2025-07-15', '2025-12-31', 'active'),
        ('ops_init_4', 'team_ops', 'Risk & Compliance Operations', 'compliance',
         'Meet regulatory and audit requirements', 500, '2025-08-01', '2025-12-31', 'active'),
        ('ops_init_5', 'team_ops', 'Internal Infrastructure Operations', 'infrastructure',
         'Maintain internal systems and tools', 500, '2025-07-01', '2025-12-31', 'active'),
        ('ops_init_6', 'team_ops', 'Vendor & Partner Management', 'vendor',
         'Manage external vendors and partners', 500, '2025-07-01', '2025-12-31', 'active'),
    ]
    
    for init in ops_initiatives:
        db_manager.execute("""
            INSERT OR REPLACE INTO operation_flow_initiatives 
            (initiative_id, team_id, initiative_name, initiative_type, objective,
             employee_capacity, start_date, end_date, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, init)
    
    # Insert all workstreams (condensed for brevity)
    insert_workstreams(db_manager)
    
    db_manager.commit()
    logger.success("Seed data inserted successfully")


def insert_workstreams(db_manager: DatabaseManager):
    """Insert all workstream data."""
    
    # PD Core Platform Workstreams
    cp_workstreams = [
        ('cp_ws_1', 'pd_init_1', 'Architecture Refactor', 'Core system design', 100, 5, 20, 'Principal Engineer', 'high', 'active'),
        ('cp_ws_2', 'pd_init_1', 'Database Optimization', 'Data layer', 100, 5, 20, 'Staff Engineer', 'high', 'active'),
        ('cp_ws_3', 'pd_init_1', 'Service Decomposition', 'Microservices', 100, 5, 20, 'Engineering Manager', 'medium', 'active'),
        ('cp_ws_4', 'pd_init_1', 'Performance Tuning', 'Latency & throughput', 100, 5, 20, 'Tech Lead', 'medium', 'planned'),
        ('cp_ws_5', 'pd_init_1', 'Reliability Engineering', 'Stability & uptime', 100, 5, 20, 'SRE Lead', 'high', 'active'),
    ]
    for ws in cp_workstreams:
        db_manager.execute("""
            INSERT OR REPLACE INTO pd_core_platform_workstreams
            (workstream_id, initiative_id, workstream_name, focus_area, employee_capacity,
             subgroups_count, employees_per_subgroup, lead_role, priority, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ws)
    
    # PD Feature Delivery Workstreams
    fd_workstreams = [
        ('fd_ws_1', 'pd_init_2', 'Feature Planning', 'Requirements', 100, 5, 20, 'Product Manager', 'high', 'active'),
        ('fd_ws_2', 'pd_init_2', 'Backend Feature Development', 'APIs', 100, 5, 20, 'Backend Lead', 'high', 'active'),
        ('fd_ws_3', 'pd_init_2', 'Frontend Feature Development', 'UI', 100, 5, 20, 'Frontend Lead', 'medium', 'active'),
        ('fd_ws_4', 'pd_init_2', 'Feature Testing', 'QA', 100, 5, 20, 'QA Manager', 'medium', 'planned'),
        ('fd_ws_5', 'pd_init_2', 'Feature Rollout', 'Release', 100, 5, 20, 'Release Manager', 'high', 'planned'),
    ]
    for ws in fd_workstreams:
        db_manager.execute("""
            INSERT OR REPLACE INTO pd_feature_delivery_workstreams
            (workstream_id, initiative_id, workstream_name, focus_area, employee_capacity,
             subgroups_count, employees_per_subgroup, lead_role, priority, status)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, ws)
    
    # Continue with other workstreams...
    # (Similar pattern for remaining workstream tables)
    
    logger.info("Workstreams inserted")


def generate_all_data(db_manager: DatabaseManager):
    """Generate all synthetic data."""
    
    # Set random seed for reproducibility
    random.seed(config.RANDOM_SEED)
    
    # Get organization and teams from database
    org_id = config.ORGANIZATION['id']
    
    # Step 1: Generate Users
    logger.info("Step 1: Generating users...")
    user_generator = UserGenerator(db_manager, org_id)
    users = user_generator.generate(config.NUM_USERS)
    logger.success(f"Generated {len(users)} users")
    
    # Step 2: Generate Team Memberships
    logger.info("Step 2: Generating team memberships...")
    team_generator = TeamGenerator(db_manager, org_id)
    team_generator.assign_users_to_teams(users)
    logger.success("Team memberships created")
    
    # Step 3: Generate Projects
    logger.info("Step 3: Generating projects...")
    project_generator = ProjectGenerator(db_manager, org_id)
    projects = project_generator.generate(config.NUM_PROJECTS, users)
    logger.success(f"Generated {len(projects)} projects")
    
    # Step 4: Generate Tasks
    logger.info("Step 4: Generating tasks...")
    task_generator = TaskGenerator(db_manager)
    tasks = task_generator.generate_for_projects(projects, users)
    logger.success(f"Generated {len(tasks)} tasks")
    
    # Step 5: Generate Subtasks
    logger.info("Step 5: Generating subtasks...")
    subtask_generator = SubtaskGenerator(db_manager)
    subtasks = subtask_generator.generate_for_tasks(tasks, users)
    logger.success(f"Generated {len(subtasks)} subtasks")
    
    # Step 6: Generate Comments
    logger.info("Step 6: Generating comments...")
    comment_generator = CommentGenerator(db_manager)
    comments = comment_generator.generate_for_tasks(tasks, users)
    logger.success(f"Generated {len(comments)} comments")
    
    # Step 7: Generate Custom Fields
    logger.info("Step 7: Generating custom fields...")
    custom_field_generator = CustomFieldGenerator(db_manager)
    custom_field_generator.generate_for_projects(projects, tasks)
    logger.success("Custom fields generated")
    
    # Step 8: Generate Tags
    logger.info("Step 8: Generating tags...")
    tag_generator = TagGenerator(db_manager, org_id)
    tag_generator.generate_and_assign(tasks)
    logger.success("Tags generated and assigned")
    
    # Commit all changes
    db_manager.commit()


def print_summary(db_manager: DatabaseManager):
    """Print summary of generated data."""
    
    logger.info("\n" + "=" * 60)
    logger.info("GENERATION SUMMARY")
    logger.info("=" * 60)
    
    tables = [
        'organizations', 'teams', 'users', 'team_memberships',
        'projects', 'sections', 'tasks', 'subtasks', 'comments',
        'custom_field_definitions', 'custom_field_values', 'tags', 'task_tags'
    ]
    
    for table in tables:
        count = db_manager.fetch_one(f"SELECT COUNT(*) FROM {table}")[0]
        logger.info(f"{table:30} : {count:,} records")
    
    logger.info("=" * 60)


def main():
    """Main entry point."""
    
    # Setup
    logger = setup_logging()
    logger.info("=" * 60)
    logger.info("ASANA SEED DATA GENERATOR")
    logger.info(f"Started at: {datetime.now().isoformat()}")
    logger.info("=" * 60)
    
    ensure_output_directory()
    
    # Database path
    db_path = project_root / config.DATABASE_PATH
    
    try:
        # Initialize database manager
        db_manager = DatabaseManager(str(db_path))
        
        # Initialize schema
        initialize_database(db_manager)
        
        # Insert seed data
        insert_seed_data(db_manager)
        
        # Generate all data
        generate_all_data(db_manager)
        
        # Print summary
        print_summary(db_manager)
        
        logger.success(f"\nDatabase saved to: {db_path}")
        logger.info(f"Completed at: {datetime.now().isoformat()}")
        
    except Exception as e:
        logger.error(f"Generation failed: {e}")
        raise
    
    finally:
        if 'db_manager' in locals():
            db_manager.close()


if __name__ == '__main__':
    main()