"""
Workstream generator for all initiative types.
"""

from datetime import datetime
import logging

logger = logging.getLogger(__name__)


class WorkstreamGenerator:
    """Generates workstream data for all initiatives."""
    
    # All workstream definitions
    WORKSTREAMS = {
        # Product Development
        "pd_core_platform_workstreams": [
            ("cp_ws_1", "pd_init_1", "Architecture Refactor", "Core system design", 100, 5, 20, "Principal Engineer", "high", "active"),
            ("cp_ws_2", "pd_init_1", "Database Optimization", "Data layer", 100, 5, 20, "Staff Engineer", "high", "active"),
            ("cp_ws_3", "pd_init_1", "Service Decomposition", "Microservices", 100, 5, 20, "Engineering Manager", "medium", "active"),
            ("cp_ws_4", "pd_init_1", "Performance Tuning", "Latency & throughput", 100, 5, 20, "Tech Lead", "medium", "planned"),
            ("cp_ws_5", "pd_init_1", "Reliability Engineering", "Stability & uptime", 100, 5, 20, "SRE Lead", "high", "active"),
        ],
        "pd_feature_delivery_workstreams": [
            ("fd_ws_1", "pd_init_2", "Feature Planning", "Requirements", 100, 5, 20, "Product Manager", "high", "active"),
            ("fd_ws_2", "pd_init_2", "Backend Feature Development", "APIs", 100, 5, 20, "Backend Lead", "high", "active"),
            ("fd_ws_3", "pd_init_2", "Frontend Feature Development", "UI", 100, 5, 20, "Frontend Lead", "medium", "active"),
            ("fd_ws_4", "pd_init_2", "Feature Testing", "QA", 100, 5, 20, "QA Manager", "medium", "planned"),
            ("fd_ws_5", "pd_init_2", "Feature Rollout", "Release", 100, 5, 20, "Release Manager", "high", "planned"),
        ],
        "pd_mobile_revamp_workstreams": [
            ("mr_ws_1", "pd_init_3", "UI Redesign", "User experience", 100, 5, 20, "UX Lead", "high", "planned"),
            ("mr_ws_2", "pd_init_3", "Performance Improvement", "App speed", 100, 5, 20, "Mobile Lead", "high", "active"),
            ("mr_ws_3", "pd_init_3", "Offline Support", "Reliability", 100, 5, 20, "Tech Lead", "medium", "planned"),
            ("mr_ws_4", "pd_init_3", "Mobile Security", "Application security", 100, 5, 20, "Security Lead", "high", "planned"),
            ("mr_ws_5", "pd_init_3", "App Store Readiness", "Deployment", 100, 5, 20, "Release Lead", "medium", "planned"),
        ],
        "pd_backend_scalability_workstreams": [
            ("bs_ws_1", "pd_init_4", "Load Handling", "Traffic spikes", 100, 5, 20, "Infra Lead", "high", "active"),
            ("bs_ws_2", "pd_init_4", "Caching Strategy", "Performance", 