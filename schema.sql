-- Enable Foreign Keys
PRAGMA foreign_keys = ON;

-- ==============================
-- 1. ORGANIZATIONS & TEAMS (Strategy Layer)
-- ==============================

CREATE TABLE IF NOT EXISTS organizations (
    organization_id TEXT PRIMARY KEY,
    name TEXT,
    domain TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS teams (
    team_id TEXT PRIMARY KEY,
    organization_id TEXT,
    name TEXT,
    team_type TEXT CHECK(team_type IN ('product', 'marketing', 'operations')),
    employee_count INTEGER,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id) ON DELETE CASCADE
);

-- ==============================
-- 2. INITIATIVES & WORKSTREAMS (Your Custom Logic)
-- ==============================
-- Note: SQLite does not support ENUM natively, using TEXT.

CREATE TABLE IF NOT EXISTS product_development_initiatives (
    initiative_id TEXT PRIMARY KEY,
    team_id TEXT,
    initiative_name TEXT,
    initiative_type TEXT,
    objective TEXT,
    employee_capacity INTEGER DEFAULT 500,
    start_date DATE,
    end_date DATE,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (team_id) REFERENCES teams(team_id) ON DELETE CASCADE
);

-- (Generic Workstream Table to capture all your specific workstream tables for linking)
-- In a real scenario, we might keep your separate tables, but for the generator 
-- to link Projects to your workstreams, we need a unified reference or we handle it in code.
-- Below are the specific workstream tables you requested.

CREATE TABLE IF NOT EXISTS pd_core_platform_workstreams (
    workstream_id TEXT PRIMARY KEY,
    initiative_id TEXT,
    workstream_name TEXT,
    focus_area TEXT,
    employee_capacity INTEGER,
    subgroups_count INTEGER,
    employees_per_subgroup INTEGER,
    lead_role TEXT,
    priority TEXT,
    status TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (initiative_id) REFERENCES product_development_initiatives(initiative_id)
);

-- ... [Ideally, we would include all other workstream tables here: pd_feature_delivery, marketing, etc.]
-- ... [For brevity in this chat, assume all your CREATE TABLE statements for workstreams are here]

-- ==============================
-- 3. EXECUTION LAYER (Asana Standard Objects)
-- ==============================

CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    organization_id TEXT,
    email TEXT UNIQUE,
    full_name TEXT,
    job_title TEXT,
    department TEXT, -- Links to your 'team_type'
    avatar_url TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    workstream_id TEXT, -- LINKS YOUR STRATEGY TO EXECUTION
    team_id TEXT,
    owner_id TEXT,
    name TEXT,
    description TEXT,
    status TEXT CHECK(status IN ('on_track', 'at_risk', 'off_track', 'on_hold', 'completed')),
    due_date DATE,
    created_at TIMESTAMP,
    archived BOOLEAN DEFAULT 0,
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (owner_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT,
    name TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT,
    section_id TEXT,
    assignee_id TEXT,
    name TEXT,
    description TEXT,
    priority TEXT CHECK(priority IN ('low', 'medium', 'high')),
    due_date DATE,
    completed BOOLEAN DEFAULT 0,
    completed_at TIMESTAMP,
    created_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id) ON DELETE CASCADE,
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

CREATE TABLE IF NOT EXISTS comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT,
    user_id TEXT,
    text_content TEXT,
    created_at TIMESTAMP,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id) ON DELETE CASCADE,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- ==============================
-- 4. SEED DATA (Your Custom Inserts)
-- ==============================

INSERT OR IGNORE INTO organizations (organization_id, name, domain)
VALUES ('org_1', 'Aasna Technologies', 'aasna.tech');

INSERT OR IGNORE INTO teams (team_id, organization_id, name, team_type, employee_count)
VALUES 
('team_pd', 'org_1', 'Product Development Team', 'product', 500),
('team_mkt', 'org_1', 'Marketing Team', 'marketing', 100),
('team_ops', 'org_1', 'Operation Flow Team', 'operations', 3000);

-- Insert Initiatives (Subset for demo)
INSERT OR IGNORE INTO product_development_initiatives VALUES
('pd_init_1', 'team_pd', 'Core Platform Modernization', 'platform', 'Upgrade core systems', 500, '2025-07-01', '2025-12-31', 'active', CURRENT_TIMESTAMP);

INSERT OR IGNORE INTO pd_core_platform_workstreams VALUES
('cp_ws_1','pd_init_1','Architecture Refactor','Core system design',100,5,20,'Principal Engineer','high','active',CURRENT_TIMESTAMP);