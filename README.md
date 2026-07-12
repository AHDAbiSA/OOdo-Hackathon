# OOdo-Hackathon
TransitOps is a smart transport operations platform that streamlines vehicle, driver, trip, maintenance, fuel, and expense management through automated workflows, real-time dashboards, business validations, and operational analytics for fleet efficiency.

# 🚛 TransitOps – Smart Transport Operations Platform

## Hour 1 Progress

### Completed
- Initialized the Odoo 18 project.
- Created the project directory structure.
- Added configuration files.
- Created the custom Odoo module `transit_ops`.
- Generated the standard Odoo module skeleton.
- Prepared the project for Authentication development.

### Next Phase
- Authentication Module
- Role-Based Access Control (RBAC)
- Login & Session Management
# TransitOps

TransitOps is a custom Odoo 18 system designed to manage and optimize transit operations, fleet management, and related workflows.

## Project Structure

This project follows a clean Odoo development layout:

- **`config/`**: System configuration files (e.g., `odoo.conf`).
- **`custom_addons/`**: Custom Odoo modules specifically developed for the TransitOps system.
- **`doc/`**: System design documentation, data models, and guides.
- **`scripts/`**: Utility scripts for database management, setups, and development helpers.

## Getting Started

### Prerequisites

- Python 3.10+
- PostgreSQL 15+
- Odoo 18.0 Community or Enterprise source code

### Installation

1. Clone this repository:
   ```bash
   git clone <repository_url> TransitOps
   cd TransitOps
   ```

2. Create a python virtual environment:
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install required packages:
   ```bash
   pip install -r requirements.txt
   ```

4. Configure the Odoo instance in `config/odoo.conf` to point to your local Odoo source directory and local PostgreSQL server.

5. Run Odoo referencing this configuration:
   ```bash
   python <path_to_odoo_bin>/odoo-bin -c config/odoo.conf
   ```

## Development Standards

- Custom modules must be kept in `custom_addons/`.
- Maintain clean, pep8-compliant Python code.
- Write XML views using clear, semantic Odoo syntax.
- Ensure all business logic is fully tested under `tests/` directories within modules.

---

# Hour 2 Progress

## ✅ Completed

- Implemented Authentication module.
- Created security groups:
  - Fleet Manager
  - Driver
  - Safety Officer
  - Financial Analyst
- Configured role-based access control (RBAC).
- Added `ir.model.access.csv`.
- Created demo users.
- Added TransitOps root menu.
- Added placeholder menus:
  - Dashboard
  - Vehicle Management
  - Driver Management
  - Trip Management
- Updated `__manifest__.py`.

## Next Phase

- Vehicle Management Module

# Hour 3 Progress

## ✅ Completed

### Vehicle Management Module

- Created `transit.vehicle` model.
- Added vehicle registration number validation.
- Implemented unique registration constraint.
- Added Tree View.
- Added Form View.
- Added Search View.
- Connected Vehicle Management menu.
- Configured Fleet Manager CRUD permissions.
- Updated module manifest.

## Next Phase

Driver Management Module

# Hour 4 Progress

## ✅ Completed

### Driver Management Module

- Created `transit.driver` model.
- Added driver license number validation.
- Implemented unique license number constraint.
- Added license expiry validation.
- Created Tree View.
- Created Form View.
- Created Search View.
- Connected Driver Management menu.
- Configured Fleet Manager CRUD permissions.
- Updated module manifest.

## Next Phase

- Trip Management Module