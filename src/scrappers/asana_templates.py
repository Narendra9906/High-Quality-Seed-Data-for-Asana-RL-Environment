"""
Asana template data
Based on public Asana template library patterns
"""

# Project templates based on Asana's public template library
PROJECT_TEMPLATES = {
    "product": {
        "sprint": [
            "Sprint {num} - {team}",
            "Q{quarter} Sprint {num}",
            "{feature} Development Sprint",
            "Release {version} Sprint"
        ],
        "kanban": [
            "{team} Engineering Board",
            "Bug Tracking - {component}",
            "Technical Debt Backlog",
            "Feature Requests"
        ],
        "timeline": [
            "{feature} Roadmap",
            "Q{quarter} Product Roadmap",
            "Platform Migration",
            "{component} Redesign"
        ],
        "list": [
            "Architecture Decisions",
            "Tech Stack Evaluation",
            "Security Audit Items",
            "Performance Optimization"
        ]
    },
    "marketing": {
        "sprint": [
            "Campaign Sprint - {campaign}",
            "Content Sprint Q{quarter}",
            "Launch Sprint - {product}"
        ],
        "kanban": [
            "Content Calendar",
            "Social Media Queue",
            "Design Requests",
            "Brand Assets"
        ],
        "timeline": [
            "{campaign} Campaign Timeline",
            "Product Launch - {product}",
            "Event Planning - {event}",
            "Rebrand Project"
        ],
        "list": [
            "Marketing Ideas Backlog",
            "Competitor Analysis",
            "Customer Testimonials",
            "Press Coverage Tracker"
        ]
    },
    "operations": {
        "sprint": [
            "Ops Sprint {num}",
            "Process Improvement Sprint",
            "Automation Sprint Q{quarter}"
        ],
        "kanban": [
            "Support Ticket Queue",
            "IT Requests",
            "Vendor Management",
            "Compliance Tasks"
        ],
        "timeline": [
            "Annual Audit Preparation",
            "System Migration",
            "Office Relocation",
            "Policy Update Rollout"
        ],
        "list": [
            "SOP Documentation",
            "Vendor Contracts",
            "Training Materials",
            "Emergency Procedures"
        ]
    }
}

# Section templates by project type
SECTION_TEMPLATES = {
    "sprint": [
        "Backlog",
        "To Do",
        "In Progress",
        "In Review",
        "Done"
    ],
    "kanban": [
        "To Do",
        "In Progress",
        "Blocked",
        "In Review",
        "Done"
    ],
    "timeline": [
        "Planning",
        "Design",
        "Development",
        "Testing",
        "Launch"
    ],
    "list": [
        "High Priority",
        "Medium Priority",
        "Low Priority",
        "Completed",
        "On Hold"
    ]
}

# Task templates by department
TASK_TEMPLATES = {
    "product": {
        "patterns": [
            "[{component}] {action} {detail}",
            "{action} {component} {detail}",
            "Implement {feature}",
            "Fix: {bug_description}",
            "Refactor {component}",
            "Add tests for {component}",
            "Update {component} documentation",
            "Review {component} performance",
            "Migrate {component} to {target}"
        ],
        "components": [
            "Auth", "API", "Database", "Cache", "Queue", "Search",
            "Notification", "Payment", "Analytics", "Dashboard",
            "User Profile", "Settings", "Admin Panel", "Reports",
            "Export", "Import", "Webhook", "Integration", "Mobile"
        ],
        "actions": [
            "Implement", "Refactor", "Optimize", "Debug", "Test",
            "Review", "Update", "Migrate", "Deploy", "Configure",
            "Monitor", "Document", "Validate", "Secure", "Scale"
        ]
    },
    "marketing": {
        "patterns": [
            "[{campaign}] {deliverable}",
            "Create {content_type} for {channel}",
            "Design {asset} for {campaign}",
            "Write {content_type}: {topic}",
            "Schedule {content_type} for {date}",
            "Analyze {metric} performance",
            "Update {asset} with new branding"
        ],
        "campaigns": [
            "Q1 Launch", "Brand Awareness", "Product Update",
            "Customer Stories", "Industry Report", "Webinar Series",
            "Email Nurture", "Social Push", "PR Campaign"
        ],
        "deliverables": [
            "Landing page", "Email sequence", "Social posts",
            "Blog article", "Case study", "Whitepaper",
            "Video script", "Infographic", "Press release"
        ]
    },
    "operations": {
        "patterns": [
            "Process {process_name}",
            "Update {document} documentation",
            "Review {area} compliance",
            "Handle {request_type} request",
            "Audit {area}",
            "Train team on {topic}",
            "Resolve {issue_type} issue"
        ],
        "processes": [
            "onboarding", "offboarding", "vendor evaluation",
            "budget review", "performance review", "incident response",
            "backup verification", "access audit", "policy update"
        ],
        "areas": [
            "security", "finance", "HR", "legal", "IT",
            "facilities", "procurement", "customer support"
        ]
    }
}


def get_project_templates(team_type: str) -> dict:
    """
    Get project templates for a specific team type
    
    Args:
        team_type: Type of team (product, marketing, operations)
        
    Returns:
        Dictionary of project templates
    """
    return PROJECT_TEMPLATES.get(team_type, PROJECT_TEMPLATES["product"])


def get_section_templates(project_type: str) -> list:
    """
    Get section templates for a project type
    
    Args:
        project_type: Type of project (sprint, kanban, timeline, list)
        
    Returns:
        List of section names
    """
    return SECTION_TEMPLATES.get(project_type, SECTION_TEMPLATES["kanban"])


def get_task_templates(team_type: str) -> dict:
    """
    Get task templates for a team type
    
    Args:
        team_type: Type of team
        
    Returns:
        Dictionary of task template data
    """
    return TASK_TEMPLATES.get(team_type, TASK_TEMPLATES["product"])