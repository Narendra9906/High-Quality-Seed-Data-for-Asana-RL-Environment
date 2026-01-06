"""
Data validation utilities for ensuring data consistency.
"""

import logging
from typing import Dict, List, Any
from datetime import datetime

logger = logging.getLogger(__name__)


def validate_database(db_manager) -> Dict[str, int]:
    """
    Validate database integrity and return record counts.
    
    Args:
        db_manager: DatabaseManager instance
        
    Returns:
        Dictionary of table names to record counts
    """
    tables = [
        "organizations",
        "teams",
        "users",
        "team_memberships",
        "product_development_initiatives",
        "marketing_initiatives",
        "operation_flow_initiatives",
        "projects",
        "sections",
        "tasks",
        "comments",
        "custom_field_definitions",
        "custom_field_values",
        "tags",
        "task_tags"
    ]
    
    counts = {}
    for table in tables:
        try:
            count = db_manager.get_count(table)
            counts[table] = count
        except Exception as e:
            logger.warning(f"Error counting {table}: {e}")
            counts[table] = 0
    
    # Run integrity checks
    _check_temporal_consistency(db_manager)
    _check_referential_integrity(db_manager)
    
    return counts


def _check_temporal_consistency(db_manager):
    """Check that temporal relationships are valid."""
    # Tasks: completed_at must be after created_at
    db_manager.execute("""
        SELECT COUNT(*) FROM tasks 
        WHERE completed_at IS NOT NULL 
        AND completed_at < created_at
    """)
    invalid_count = db_manager.fetchone()[0]
    if invalid_count > 0:
        logger.warning(f"Found {invalid_count} tasks with completed_at before created_at")
    
    # Tasks: completed_at should only exist if completed = 1
    db_manager.execute("""
        SELECT COUNT(*) FROM tasks 
        WHERE completed = 0 
        AND completed_at IS NOT NULL
    """)
    invalid_count = db_manager.fetchone()[0]
    if invalid_count > 0:
        logger.warning(f"Found {invalid_count} incomplete tasks with completed_at set")


def _check_referential_integrity(db_manager):
    """Check that foreign key relationships are valid."""
    # Tasks must reference valid projects
    db_manager.execute("""
        SELECT COUNT(*) FROM tasks t
        LEFT JOIN projects p ON t.project_id = p.project_id
        WHERE t.project_id IS NOT NULL AND p.project_id IS NULL
    """)
    invalid_count = db_manager.fetchone()[0]
    if invalid_count > 0:
        logger.warning(f"Found {invalid_count} tasks with invalid project_id")
    
    # Tasks must reference valid sections (if set)
    db_manager.execute("""
        SELECT COUNT(*) FROM tasks t
        LEFT JOIN sections s ON t.section_id = s.section_id
        WHERE t.section_id IS NOT NULL AND s.section_id IS NULL
    """)
    invalid_count = db_manager.fetchone()[0]
    if invalid_count > 0:
        logger.warning(f"Found {invalid_count} tasks with invalid section_id")
    
    # Task sections must belong to same project
    db_manager.execute("""
        SELECT COUNT(*) FROM tasks t
        JOIN sections s ON t.section_id = s.section_id
        WHERE t.project_id != s.project_id
    """)
    invalid_count = db_manager.fetchone()[0]
    if invalid_count > 0:
        logger.warning(f"Found {invalid_count} tasks in sections from different projects")


def validate_task(task: Dict[str, Any]) -> List[str]:
    """
    Validate a single task record.
    
    Args:
        task: Task data dictionary
        
    Returns:
        List of validation error messages (empty if valid)
    """
    errors = []
    
    # Required fields
    if not task.get("task_id"):
        errors.append("task_id is required")
    if not task.get("name"):
        errors.append("name is required")
    
    # Temporal consistency
    created_at = task.get("created_at")
    completed_at = task.get("completed_at")
    
    if completed_at and created_at:
        if isinstance(created_at, str):
            created_at = datetime.fromisoformat(created_at)
        if isinstance(completed_at, str):
            completed_at = datetime.fromisoformat(completed_at)
        
        if completed_at < created_at:
            errors.append("completed_at must be after created_at")
    
    # Completion consistency
    if task.get("completed") and not completed_at:
        errors.append("completed_at required when completed is True")
    if not task.get("completed") and completed_at:
        errors.append("completed_at should be None when not completed")
    
    return errors


def validate_date_range(start_date, end_date) -> bool:
    """Validate that start_date is before end_date."""
    if start_date is None or end_date is None:
        return True
    
    if isinstance(start_date, str):
        start_date = datetime.fromisoformat(start_date)
    if isinstance(end_date, str):
        end_date = datetime.fromisoformat(end_date)
    
    return start_date <= end_date