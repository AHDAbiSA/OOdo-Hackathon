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
