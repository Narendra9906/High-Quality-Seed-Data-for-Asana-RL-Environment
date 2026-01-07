-- ==============================
-- ASANA SEED DATA GENERATOR
-- SQLite Compatible Schema
-- ==============================

DROP TABLE IF EXISTS task_tags;
DROP TABLE IF EXISTS tags;
DROP TABLE IF EXISTS custom_field_values;
DROP TABLE IF EXISTS custom_field_definitions;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS subtasks;
DROP TABLE IF EXISTS tasks;
DROP TABLE IF EXISTS sections;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS team_memberships;
DROP TABLE IF EXISTS users;

-- Drop workstream tables
DROP TABLE IF EXISTS ops_vendor_workstreams;
DROP TABLE IF EXISTS ops_infrastructure_workstreams;
DROP TABLE IF EXISTS ops_compliance_workstreams;
DROP TABLE IF EXISTS ops_finance_workstreams;
DROP TABLE IF EXISTS ops_customer_support_workstreams;
DROP TABLE IF EXISTS ops_process_optimization_workstreams;
DROP TABLE IF EXISTS operation_flow_initiatives;

DROP TABLE IF EXISTS mkt_operations_workstreams;
DROP TABLE IF EXISTS mkt_retention_workstreams;
DROP TABLE IF EXISTS mkt_performance_workstreams;
DROP TABLE IF EXISTS mkt_content_workstreams;
DROP TABLE IF EXISTS mkt_growth_workstreams;
DROP TABLE IF EXISTS mkt_product_launch_workstreams;
DROP TABLE IF EXISTS mkt_brand_awareness_workstreams;
DROP TABLE IF EXISTS marketing_initiatives;

DROP TABLE IF EXISTS pd_dev_experience_workstreams;
DROP TABLE IF EXISTS pd_security_compliance_workstreams;
DROP TABLE IF EXISTS pd_api_integration_workstreams;
DROP TABLE IF EXISTS pd_backend_scalability_workstreams;
DROP TABLE IF EXISTS pd_mobile_revamp_workstreams;
DROP TABLE IF EXISTS pd_feature_delivery_workstreams;
DROP TABLE IF EXISTS pd_core_platform_workstreams;
DROP TABLE IF EXISTS product_development_initiatives;

DROP TABLE IF EXISTS teams;
DROP TABLE IF EXISTS organizations;

-- ==============================
-- 1. ORGANIZATIONS TABLE
-- ==============================
CREATE TABLE organizations (
    organization_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==============================
-- 2. TEAMS TABLE
-- ==============================
CREATE TABLE teams (
    team_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    team_type TEXT CHECK(team_type IN ('product', 'marketing', 'operations')),
    employee_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id) ON DELETE CASCADE
);

-- ==============================
-- 3. USERS TABLE
-- ==============================
CREATE TABLE users (
    user_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    full_name TEXT NOT NULL,
    job_title TEXT,
    department TEXT,
    is_active INTEGER DEFAULT 1,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    last_login_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id) ON DELETE CASCADE
);

-- ==============================
-- 4. TEAM MEMBERSHIPS TABLE
-- ==============================
CREATE TABLE team_memberships (
    membership_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    role TEXT CHECK(role IN ('member', 'lead', 'admin')) DEFAULT 'member',
    joined_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id) ON DELETE CASCADE,
    UNIQUE(team_id, user_id)
);

-- ==============================
-- 5. PRODUCT DEVELOPMENT INITIATIVES TABLE
-- ==============================
CREATE TABLE product_development_initiatives (
    initiative_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    initiative_name TEXT NOT NULL,
    initiative_type TEXT CHECK(initiative_type IN ('platform', 'feature', 'infra', 'security')),
    objective TEXT,
    employee_capacity INTEGER DEFAULT 500,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'active', 'completed')) DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- ==============================
-- 6. PRODUCT DEVELOPMENT WORKSTREAMS
-- ==============================

-- Core Platform Workstreams
CREATE TABLE pd_core_platform_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- Feature Delivery Workstreams
CREATE TABLE pd_feature_delivery_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- Mobile Revamp Workstreams
CREATE TABLE pd_mobile_revamp_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- Backend Scalability Workstreams
CREATE TABLE pd_backend_scalability_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- API Integration Workstreams
CREATE TABLE pd_api_integration_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- Security Compliance Workstreams
CREATE TABLE pd_security_compliance_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- Developer Experience Workstreams
CREATE TABLE pd_dev_experience_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id) ON DELETE CASCADE
);

-- ==============================
-- 7. MARKETING INITIATIVES TABLE
-- ==============================
CREATE TABLE marketing_initiatives (
    initiative_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    initiative_name TEXT NOT NULL,
    initiative_type TEXT CHECK(initiative_type IN ('branding', 'launch', 'growth', 'content', 'performance', 'retention', 'operations')),
    objective TEXT,
    employee_capacity INTEGER DEFAULT 500,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'active', 'completed')) DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- ==============================
-- 8. MARKETING WORKSTREAMS
-- ==============================

-- Brand Awareness Workstreams
CREATE TABLE mkt_brand_awareness_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- Product Launch Workstreams
CREATE TABLE mkt_product_launch_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- Growth Workstreams
CREATE TABLE mkt_growth_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- Content Workstreams
CREATE TABLE mkt_content_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- Performance Workstreams
CREATE TABLE mkt_performance_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- Retention Workstreams
CREATE TABLE mkt_retention_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- Marketing Operations Workstreams
CREATE TABLE mkt_operations_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES marketing_initiatives(initiative_id) ON DELETE CASCADE
);

-- ==============================
-- 9. OPERATION FLOW INITIATIVES TABLE
-- ==============================
CREATE TABLE operation_flow_initiatives (
    initiative_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    initiative_name TEXT NOT NULL,
    initiative_type TEXT CHECK(initiative_type IN ('process', 'customer_support', 'finance', 'compliance', 'infrastructure', 'vendor')),
    objective TEXT,
    employee_capacity INTEGER DEFAULT 500,
    start_date DATE,
    end_date DATE,
    status TEXT CHECK(status IN ('planned', 'active', 'completed')) DEFAULT 'planned',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- ==============================
-- 10. OPERATIONS WORKSTREAMS
-- ==============================

-- Process Optimization Workstreams
CREATE TABLE ops_process_optimization_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES operation_flow_initiatives(initiative_id) ON DELETE CASCADE
);

-- Customer Support Workstreams
CREATE TABLE ops_customer_support_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES operation_flow_initiatives(initiative_id) ON DELETE CASCADE
);

-- Finance Workstreams
CREATE TABLE ops_finance_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES operation_flow_initiatives(initiative_id) ON DELETE CASCADE
);

-- Compliance Workstreams
CREATE TABLE ops_compliance_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES operation_flow_initiatives(initiative_id) ON DELETE CASCADE
);

-- Infrastructure Workstreams
CREATE TABLE ops_infrastructure_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES operation_flow_initiatives(initiative_id) ON DELETE CASCADE
);

-- Vendor Workstreams
CREATE TABLE ops_vendor_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT NOT NULL,
    workstream_name TEXT NOT NULL,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    status TEXT CHECK(status IN ('planned', 'active', 'completed')),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES operation_flow_initiatives(initiative_id) ON DELETE CASCADE
);

-- ==============================
-- 11. PROJECTS TABLE
-- ==============================
CREATE TABLE projects (
    project_id TEXT PRIMARY KEY,
    team_id TEXT NOT NULL,
    workstream_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    color TEXT,
    status TEXT CHECK(status IN ('active', 'on_hold', 'completed', 'archived')) DEFAULT 'active',
    privacy TEXT CHECK(privacy IN ('public', 'private')) DEFAULT 'public',
    owner_id TEXT,
    start_date DATE,
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE,
    FOREIGN KEY (owner_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- ==============================
-- 12. SECTIONS TABLE
-- ==============================
CREATE TABLE sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- ==============================
-- 13. TASKS TABLE
-- ==============================
CREATE TABLE tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    assignee_id TEXT,
    due_date DATE,
    start_date DATE,
    completed INTEGER DEFAULT 0,
    completed_at TIMESTAMP,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    created_by TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES sections(section_id) ON DELETE SET NULL,
    FOREIGN KEY (assignee_id) REFERENCES users(user_id) ON DELETE SET NULL,
    FOREIGN KEY (created_by) REFERENCES users(user_id) ON DELETE SET NULL
);

-- ==============================
-- 14. SUBTASKS TABLE
-- ==============================
CREATE TABLE subtasks (
    subtask_id TEXT PRIMARY KEY,
    parent_task_id TEXT NOT NULL,
    name TEXT NOT NULL,
    description TEXT,
    assignee_id TEXT,
    due_date DATE,
    completed INTEGER DEFAULT 0,
    completed_at TIMESTAMP,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
    FOREIGN KEY (assignee_id) REFERENCES users(user_id) ON DELETE SET NULL
);

-- ==============================
-- 15. COMMENTS TABLE
-- ==============================
CREATE TABLE comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    author_id TEXT NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
    FOREIGN KEY (author_id) REFERENCES users(user_id) ON DELETE CASCADE
);

-- ==============================
-- 16. CUSTOM FIELD DEFINITIONS TABLE
-- ==============================
CREATE TABLE custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT CHECK(field_type IN ('text', 'number', 'enum', 'date', 'people')) NOT NULL,
    enum_options TEXT,  -- JSON array for enum options
    is_required INTEGER DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

-- ==============================
-- 17. CUSTOM FIELD VALUES TABLE
-- ==============================
CREATE TABLE custom_field_values (
    value_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    field_id TEXT NOT NULL,
    text_value TEXT,
    number_value REAL,
    date_value DATE,
    enum_value TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id) ON DELETE CASCADE,
    UNIQUE(task_id, field_id)
);

-- ==============================
-- 18. TAGS TABLE
-- ==============================
CREATE TABLE tags (
    tag_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    color TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id) ON DELETE CASCADE
);

-- ==============================
-- 19. TASK-TAG ASSOCIATIONS TABLE
-- ==============================
CREATE TABLE task_tags (
    task_tag_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id) ON DELETE CASCADE,
    UNIQUE(task_id, tag_id)
);

-- ==============================
-- CREATE INDEXES FOR PERFORMANCE
-- ==============================
CREATE INDEX idx_users_org ON users(organization_id);
CREATE INDEX idx_users_email ON users(email);
CREATE INDEX idx_team_memberships_team ON team_memberships(team_id);
CREATE INDEX idx_team_memberships_user ON team_memberships(user_id);
CREATE INDEX idx_projects_team ON projects(team_id);
CREATE INDEX idx_projects_owner ON projects(owner_id);
CREATE INDEX idx_sections_project ON sections(project_id);
CREATE INDEX idx_tasks_project ON tasks(project_id);
CREATE INDEX idx_tasks_section ON tasks(section_id);
CREATE INDEX idx_tasks_assignee ON tasks(assignee_id);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
CREATE INDEX idx_tasks_completed ON tasks(completed);
CREATE INDEX idx_subtasks_parent ON subtasks(parent_task_id);
CREATE INDEX idx_comments_task ON comments(task_id);
CREATE INDEX idx_comments_author ON comments(author_id);
CREATE INDEX idx_custom_field_values_task ON custom_field_values(task_id);
CREATE INDEX idx_task_tags_task ON task_tags(task_id);
CREATE INDEX idx_task_tags_tag ON task_tags(tag_id);