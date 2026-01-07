"""
Configuration settings for Asana Seed Data Generator.

This file contains all configurable parameters for generating the seed data.
Adjust these values to control the scale and characteristics of the generated data.
"""

import os
from datetime import datetime, timedelta
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# ======================
# SCALE CONFIGURATION
# ======================

# Number of users to generate (demo scale: 100)
NUM_USERS = 100

# Number of projects to generate (demo scale: 175)
NUM_PROJECTS = 175

# Tasks per project range
MIN_TASKS_PER_PROJECT = 15
MAX_TASKS_PER_PROJECT = 30

# Subtasks per task range (not all tasks have subtasks)
MIN_SUBTASKS_PER_TASK = 0
MAX_SUBTASKS_PER_TASK = 5
SUBTASK_PROBABILITY = 0.4  # 40% of tasks have subtasks

# Comments per task range
MIN_COMMENTS_PER_TASK = 0
MAX_COMMENTS_PER_TASK = 8
COMMENT_PROBABILITY = 0.6  # 60% of tasks have comments

# Sections per project
MIN_SECTIONS_PER_PROJECT = 3
MAX_SECTIONS_PER_PROJECT = 7

# ======================
# ORGANIZATION CONFIG
# ======================

ORGANIZATION = {
    'id': 'org_1',
    'name': 'Aasna Technologies',
    'domain': 'fintech'
}

# ======================
# TEAM CONFIGURATION
# ======================

TEAMS = [
    {
        'id': 'team_pd',
        'name': 'Product Development Team',
        'type': 'product',
        'employee_count': 3500,
        'user_percentage': 0.50  # 50% of users
    },
    {
        'id': 'team_mkt',
        'name': 'Marketing Team',
        'type': 'marketing',
        'employee_count': 1500,
        'user_percentage': 0.25  # 25% of users
    },
    {
        'id': 'team_ops',
        'name': 'Operations Team',
        'type': 'operations',
        'employee_count': 3000,
        'user_percentage': 0.25  # 25% of users
    }
]

# ======================
# DATE CONFIGURATION
# ======================

# Historical data range (6 months back from today)
DATE_RANGE_MONTHS = 6
START_DATE = datetime.now() - timedelta(days=DATE_RANGE_MONTHS * 30)
END_DATE = datetime.now()

# Future due dates range (up to 3 months ahead)
FUTURE_DATE_MONTHS = 3
MAX_FUTURE_DATE = datetime.now() + timedelta(days=FUTURE_DATE_MONTHS * 30)

# ======================
# TASK DISTRIBUTION
# ======================

# Due date distribution (based on Asana research)
DUE_DATE_DISTRIBUTION = {
    'within_1_week': 0.25,
    'within_1_month': 0.40,
    'within_3_months': 0.20,
    'no_due_date': 0.10,
    'overdue': 0.05
}

# Task completion rates by project type
COMPLETION_RATES = {
    'sprint': (0.70, 0.85),      # 70-85% completed
    'bug_tracking': (0.60, 0.70), # 60-70% completed
    'ongoing': (0.40, 0.50),      # 40-50% completed
    'default': (0.50, 0.65)       # 50-65% completed
}

# Unassigned task percentage (per Asana benchmarks)
UNASSIGNED_TASK_PERCENTAGE = 0.15

# ======================
# USER DISTRIBUTION
# ======================

# Job titles by department
JOB_TITLES = {
    'product': [
        'Software Engineer', 'Senior Software Engineer', 'Staff Engineer',
        'Principal Engineer', 'Engineering Manager', 'Tech Lead',
        'Product Manager', 'Senior Product Manager', 'Director of Engineering',
        'DevOps Engineer', 'SRE', 'QA Engineer', 'Frontend Engineer',
        'Backend Engineer', 'Full Stack Engineer', 'Mobile Engineer',
        'Data Engineer', 'ML Engineer', 'Security Engineer', 'Platform Engineer'
    ],
    'marketing': [
        'Marketing Manager', 'Brand Manager', 'Content Strategist',
        'SEO Specialist', 'Growth Manager', 'Marketing Analyst',
        'Social Media Manager', 'Product Marketing Manager', 'Creative Director',
        'Copywriter', 'Digital Marketing Specialist', 'Campaign Manager',
        'Marketing Operations Manager', 'Performance Marketing Manager',
        'Email Marketing Specialist', 'Event Manager', 'PR Manager'
    ],
    'operations': [
        'Operations Manager', 'Customer Success Manager', 'Support Engineer',
        'Account Manager', 'Finance Analyst', 'HR Manager', 'Recruiter',
        'Office Manager', 'Legal Counsel', 'Compliance Officer',
        'Project Coordinator', 'Business Analyst', 'Process Improvement Manager',
        'Vendor Manager', 'Procurement Specialist', 'Risk Analyst'
    ]
}

# ======================
# LLM CONFIGURATION
# ======================

GROQ_API_KEY = os.getenv('GROQ_API_KEY', '')
LLM_MODEL = os.getenv('LLM_MODEL', 'llama-3.1-70b-versatile')
API_CALL_DELAY = float(os.getenv('API_CALL_DELAY', '0.5'))
MAX_RETRIES = int(os.getenv('MAX_RETRIES', '3'))

# Temperature settings for different content types
LLM_TEMPERATURES = {
    'task_names': 0.7,
    'task_descriptions': 0.8,
    'comments': 0.9,
    'project_names': 0.6
}

# ======================
# DATABASE CONFIGURATION
# ======================

DATABASE_PATH = os.getenv('DATABASE_PATH', 'output/asana_simulation.sqlite')

# ======================
# MISC SETTINGS
# ======================

DEBUG_MODE = os.getenv('DEBUG_MODE', 'false').lower() == 'true'
RANDOM_SEED = int(os.getenv('RANDOM_SEED', '42'))

# Colors for projects (Asana palette)
PROJECT_COLORS = [
    'dark-pink', 'dark-green', 'dark-blue', 'dark-red', 'dark-teal',
    'dark-brown', 'dark-orange', 'dark-purple', 'dark-warm-gray',
    'light-pink', 'light-green', 'light-blue', 'light-red', 'light-teal',
    'light-yellow', 'light-orange', 'light-purple', 'light-warm-gray'
]

# Tag colors
TAG_COLORS = [
    'dark-pink', 'dark-green', 'dark-blue', 'dark-red', 'dark-teal',
    'light-pink', 'light-green', 'light-blue', 'light-orange', 'light-purple'
]

# Section name templates by project type
SECTION_TEMPLATES = {
    'product': ['Backlog', 'To Do', 'In Progress', 'In Review', 'Done', 'Blocked'],
    'marketing': ['Planning', 'In Progress', 'Review', 'Approved', 'Published', 'Archived'],
    'operations': ['New', 'Assigned', 'In Progress', 'Pending Approval', 'Completed', 'On Hold']
}