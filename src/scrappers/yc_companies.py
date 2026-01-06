"""
Scraper for Y Combinator company data
Used to generate realistic B2B SaaS company and project names
"""
import json
import os
from pathlib import Path

# Pre-scraped YC company data for offline use
YC_COMPANIES = [
    "Stripe", "Airbnb", "Dropbox", "Coinbase", "Instacart",
    "DoorDash", "Gusto", "Zapier", "GitLab", "Segment",
    "Retool", "Notion", "Figma", "Linear", "Vercel",
    "PlanetScale", "Railway", "Supabase", "Resend", "Clerk",
    "Neon", "Temporal", "Dbt", "Airbyte", "Dagster",
    "Prefect", "Modal", "Replicate", "Anthropic", "Cohere",
    "Hugging Face", "Scale AI", "Weights & Biases", "Labelbox",
    "Snorkel", "Monte Carlo", "Fivetran", "Census", "Hightouch",
    "Rudderstack", "Amplitude", "Mixpanel", "Heap", "PostHog",
    "Pendo", "Whatfix", "Intercom", "Zendesk", "Freshworks"
]

# B2B SaaS product/project name components
PRODUCT_PREFIXES = [
    "Core", "Enterprise", "Pro", "Plus", "Cloud", "Smart",
    "Next", "Ultra", "Prime", "Elite", "Advanced", "Premium"
]

PRODUCT_DOMAINS = [
    "Analytics", "Dashboard", "Portal", "Hub", "Platform",
    "Suite", "System", "Engine", "Manager", "Tracker",
    "Monitor", "Connector", "Gateway", "Bridge", "Link"
]


def get_company_names(count: int = 50) -> list:
    """
    Get realistic company names for simulation
    
    Args:
        count: Number of company names to return
        
    Returns:
        List of company name strings
    """
    # Check for cached data
    cache_path = Path("data/companies.json")
    if cache_path.exists():
        with open(cache_path, 'r') as f:
            cached = json.load(f)
            return cached[:count]
    
    # Return pre-scraped data
    return YC_COMPANIES[:count]


def get_product_names(count: int = 50) -> list:
    """
    Generate realistic B2B SaaS product names
    
    Args:
        count: Number of product names to generate
        
    Returns:
        List of product name strings
    """
    import random
    
    names = []
    for _ in range(count):
        prefix = random.choice(PRODUCT_PREFIXES)
        domain = random.choice(PRODUCT_DOMAINS)
        names.append(f"{prefix} {domain}")
    
    return names


def get_feature_names() -> list:
    """
    Get realistic feature names for tasks
    
    Returns:
        List of feature name strings
    """
    return [
        "User Authentication", "Dashboard Redesign", "API Gateway",
        "Search Optimization", "Notification System", "Payment Integration",
        "Report Generator", "Data Export", "Bulk Import", "SSO Integration",
        "Role Management", "Audit Logging", "Rate Limiting", "Caching Layer",
        "Real-time Updates", "Mobile Responsiveness", "Dark Mode", "Localization",
        "Accessibility", "Performance Optimization", "Security Hardening",
        "Database Migration", "API Versioning", "Webhook System", "Email Templates"
    ]