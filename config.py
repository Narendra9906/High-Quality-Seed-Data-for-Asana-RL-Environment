import os
from pathlib import Path

# Base Paths
BASE_DIR = Path(__file__).resolve().parent
DB_PATH = BASE_DIR / "output" / "asana_simulation.sqlite"
SCHEMA_PATH = BASE_DIR / "schema.sql"
OUTPUT_DIR = BASE_DIR / "output"

# Simulation Scale (Demo Config)
NUM_USERS = 100
NUM_PROJECTS = 175
AVG_TASKS_PER_PROJECT = 12  # Adjusted to keep generation fast for demo
AVG_SUBTASKS_PER_TASK = 2

# Company Details
COMPANY_NAME = "Aasna Technologies"
DOMAIN = "aasna.tech"

# Date Settings
SIMULATION_START_DATE = "2025-01-01"
SIMULATION_END_DATE = "2026-06-30"

# Random Seed for Reproducibility
RANDOM_SEED = 42