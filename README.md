# High-Quality-Seed-Data-for-Asana-RL-Environment
I am going to create a realistic seed dataset simulating a company's Asana workspace.


## **Complete Repository Structure - Detailed Explanation** 🌳
```
asana-seed-data-generator/
│
├── README.md                          # Project overview, setup guide
│   # Contains: What this is, how to run, requirements
│
├── requirements.txt                   # Python packages needed
│   # pandas, anthropic, sqlite3, faker, etc.
│
├── schema.sql                         # Database structure (CREATE TABLE statements)
│   # All tables defined here with columns, types, constraints
│
├── .env.example                       # Example environment variables
│   # ANTHROPIC_API_KEY=your_key_here
│
├── config.py                          # Configuration settings
│   # NUM_USERS=150, NUM_PROJECTS=50, etc.
│
├── src/                               # Main source code
│   │
│   ├── main.py                        # Entry point - orchestrates everything
│   │   # Calls all generators in order, saves to DB
│   │
│   ├── scrapers/                      # Fetch real-world data
│   │   ├── __init__.py
│   │   ├── yc_companies.py           # Scrape Y Combinator companies
│   │   ├── census_names.py           # Load US Census name data
│   │   └── asana_templates.py        # Parse public Asana templates
│   │
│   ├── generators/                    # Generate fake data
│   │   ├── __init__.py
│   │   ├── users.py                  # Generate users (150)
│   │   ├── teams.py                  # Generate teams (Engineering, etc.)
│   │   ├── projects.py               # Generate projects (50)
│   │   ├── tasks.py                  # Generate tasks (2000) - uses LLM
│   │   ├── subtasks.py               # Generate subtasks
│   │   ├── comments.py               # Generate comments - uses LLM
│   │   ├── custom_fields.py          # Generate custom field definitions
│   │   └── tags.py                   # Generate tags
│   │
│   ├── models/                        # Data structure definitions
│   │   ├── __init__.py
│   │   ├── user.py                   # User dataclass
│   │   ├── team.py                   # Team dataclass
│   │   ├── project.py                # Project dataclass
│   │   ├── task.py                   # Task dataclass
│   │   └── comment.py                # Comment dataclass
│   │
│   └── utils/                         # Helper functions
│       ├── __init__.py
│       ├── date_utils.py             # Date generation, validation
│       ├── llm_utils.py              # Claude API calls
│       ├── name_generator.py         # Name generation logic
│       ├── prompt_loader.py          # Load prompts from files
│       ├── validators.py             # Data validation functions
│       └── db_utils.py               # Database helper functions
│
├── prompts/                           # LLM prompt templates
│   ├── tasks_engineering.txt         # Engineering task generation
│   ├── tasks_marketing.txt           # Marketing task generation
│   ├── tasks_operations.txt          # Operations task generation
│   ├── task_descriptions.txt         # Task description generation
│   ├── comments.txt                  # Comment generation
│   └── project_names.txt             # Project name generation
│
├── data/                              # Static data files
│   ├── first_names.csv               # US Census first names
│   ├── last_names.csv                # US Census last names
│   └── companies.json                # Scraped company names
│
├── tests/                             # Unit tests (optional but good!)
│   ├── test_generators.py
│   ├── test_validators.py
│   └── test_utils.py
│
└── output/                            # Generated files
    ├── asana_simulation.sqlite       # Final database (submit this!)
    └── generation_log.txt            # Logs from generation process
