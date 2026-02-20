# CRM Kitty Backend

![Version](https://img.shields.io/badge/version-0.0.1-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![Python](https://img.shields.io/badge/python-3.8%2B-blue)

## Introduction

CRM Kitty Backend is a modern Customer Relationship Management (CRM) API built with **FastAPI** and **SQLAlchemy**. It provides a robust, scalable backend infrastructure for managing customer data, leads, invoices, products, activities, and relationships. This project is designed to streamline business operations with features like user authentication, role-based access control, activity logging, and comprehensive reporting.

### Key Features
- 🔐 **Authentication & Authorization** - JWT-based authentication with role-based access control
- 👥 **Customer Management** - Full CRUD operations for customer data
- 📊 **Lead Management** - Track and manage sales leads
- 📝 **Invoice Management** - Create and manage invoices
- 📦 **Product Catalog** - Manage product inventory
- 📅 **Follow-up Tracking** - Schedule and track customer follow-ups
- 📋 **Activity Logging** - Automatic logging of all user activities
- 📈 **Reporting** - Generate insightful business reports
- 🏢 **Multi-company Support** - Manage multiple companies within a single instance

### Technology Stack
- **Framework**: [FastAPI](https://fastapi.tiangolo.com/) - Modern Python web framework
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/) - SQL toolkit and ORM
- **Database**: SQLite (configurable via environment variables)
- **Validation**: [Pydantic](https://pydantic-settings.readthedocs.io/) - Data validation using Python type annotations
- **Migrations**: [Alembic](https://alembic.sqlalchemy.org/) - Database schema management
- **Server**: [Uvicorn](https://www.uvicorn.org/) - ASGI web server
- **Testing**: [Pytest](https://pytest.org/) - Testing framework

### Supported Operating Systems
- Windows 10 and above
- macOS 10.14 and above
- Linux (Ubuntu 18.04+, CentOS 7+, Debian 10+)

### Python Version Requirements
- Python 3.8 or higher

---

## Getting Started

### Prerequisites

Before you begin, ensure you have the following installed on your system:

- **Python 3.8+** - [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python) - [pip documentation](https://pip.pypa.io/en/latest/)
- **Git** - [Download Git](https://git-scm.com/)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/aniket-toro/CRMKitty.git
   cd CRMKitty
   ```

2. **Create a virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requiremet.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the backend directory with the following variables:
   ```env
   ALGORITHM=HS256
   SECRET_KEY=your-secret-key-here
   ACCESS_TOKEN_TIME=30
   REFRESH_TOKEN_TIME=1800
   BASEURL=http://localhost:8000/api
   SYSTEM_USER=admin
   SYSTEM_PWD=admin
   ```

5. **Run database migrations**
   ```bash
   alembic revison --autogenerate -m "new migration"
   alembic upgrade head
   ```

6. **Seed the database (optional)**
   ```bash
   python seed.py
   ```

### Running the Application

Start the development server:

```bash
# Using Uvicorn directly
uvicorn main:app --reload

# Using Python
python -m uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`

### API Documentation

Once the server is running, access the interactive API documentation:
- **Swagger UI**: [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc**: [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Basic Usage Example

```python
import requests

BASE_URL = "http://localhost:8000/api"

# Authenticate and get access token
auth_response = requests.post(
    f"{BASE_URL}/auth/token",
    data={"username": "admin", "password": "admin"}
)
token = auth_response.json()["access_token"]

# Create a new customer
headers = {"Authorization": f"Bearer {token}"}
customer_data = {
    "first_name": "John",
    "last_name": "Doe",
    "email": "john.doe@example.com"
}

response = requests.post(
    f"{BASE_URL}/customer",
    json=customer_data,
    headers=headers
)

print(response.status_code)  # 201
print(response.json())       # Customer details
```

---

## Development Setup

### Prerequisites for Development

In addition to the standard prerequisites, you'll need:
- A code editor (VS Code, PyCharm, etc.)
- Git for version control
- Postman or similar tool for API testing (optional)

### Building from Source

1. **Clone and setup** (follow the Installation steps above)

2. **Install development dependencies**
   ```bash
   pip install -r requiremet.txt
   pip install pytest pytest-cov black flake8
   ```

3. **Project Structure**
   ```
   backend/
   ├── apis/              # API route handlers (v1 routers)
   ├── core/              # Configuration and utilities
   ├── db/                # Database models, repositories, and seeding
   │   ├── models/        # SQLAlchemy models
   │   ├── repository/    # Data access layer
   │   └── seed/          # Database seeding scripts
   ├── schemas/           # Pydantic schemas for request/response validation
   ├── services/          # Business logic layer
   ├── tests/             # Test suite
   ├── alembic/           # Database migration files
   ├── main.py            # Application entry point
   └── requiremet.txt     # Project dependencies
   ```

### Running Tests

Execute the test suite to verify everything is working correctly:

```bash
# Run all tests
pytest

# Run tests with coverage report
pytest --cov=.

# Run specific test file
pytest tests/customers/test_customers.py

# Run tests with verbose output
pytest -v

# Run tests for specific module
pytest tests/users/ -v
```

**Available Test Modules:**
- `tests/customers/` - Customer management tests
- `tests/users/` - User and role management tests
- `tests/leads/` - Lead management tests
- `tests/products/` - Product management tests
- `tests/invoice/` - Invoice management tests
- `tests/reports/` - Reporting functionality tests

### Setting Up Test Environment

Create a `.env.test` file with test configuration:
```env
ALGORITHM=HS256
SECRET_KEY=test-secret-key
ACCESS_TOKEN_TIME=30
REFRESH_TOKEN_TIME=1800
BASEURL=http://localhost:8000/api
SYSTEM_USER=admin
SYSTEM_PWD=admin
```

### Database Migrations

**Creating a new migration:**
```bash
alembic revision --autogenerate -m "Migration description"
alembic upgrade head
```

**Viewing migration history:**
```bash
alembic history
```

**Reverting migrations:**
```bash
alembic downgrade -1
```

All migration files are stored in `alembic/versions/`

### Code Quality

We recommend following these practices:

**Format code with Black:**
```bash
black .
```

**Lint code with Flake8:**
```bash
flake8 . --max-line-length=100
```

---

## Contributing

We welcome contributions to CRM Kitty! Whether you're reporting bugs, suggesting features, or submitting code improvements, your help is appreciated.

### Reporting Issues

Found a bug or have a feature request? Please open an issue on our GitHub repository:

1. Go to the [Issues page](../../issues)
2. Click "New Issue"
3. Provide a clear title and detailed description
4. Include steps to reproduce (for bugs) or use case (for features)
5. Add relevant labels (bug, enhancement, documentation, etc.)

### Contributing Code

#### Getting Started with Contributing

1. **Fork the repository** and create a feature branch
   ```bash
   git checkout -b feature/your-feature-name
   ```

2. **Make your changes** following the code style guidelines below

3. **Write tests** for new functionality
   ```bash
   # Example test structure
   pytest tests/path/to/test_feature.py
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m "feat: add new feature description"
   git commit -m "fix: resolve bug description"
   ```

5. **Push to your fork** and open a Pull Request
   ```bash
   git push origin feature/your-feature-name
   ```

#### Coding Guidelines

- Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/) style guide
- Use type hints for function arguments and return values
- Write docstrings for all functions and classes
- Keep functions small and focused on a single responsibility
- Write tests for all new features (minimum 80% coverage)

#### Pull Request Process

1. Update the [README.md](README.md) with details of changes (if applicable)
2. Ensure all tests pass: `pytest`
3. Code should be formatted with Black: `black .`
4. Run Flake8 linter: `flake8 .`
5. Get approval from at least one maintainer
6. Ensure commits are squashed and messages are clear

#### Commit Message Format

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Types**: feat, fix, docs, style, refactor, test, chore
**Scope**: The part of the code affected (e.g., customers, auth, database)

Example:
```
feat(customers): add email validation to customer creation

Add regex-based email validation using pydantic validators
to ensure valid email formats during customer creation.

Closes #123
```

### Community Code of Conduct

We are committed to providing a welcoming and inclusive environment. All contributors and participants are expected to:

- Be respectful of different opinions and experiences
- Provide constructive feedback
- Focus on what is best for the community
- Show empathy towards other community members

Instances of abusive, harassing, or otherwise unacceptable behavior may be reported by contacting the project maintainers.

### Questions or Need Help?

- 📧 **Email**: Contact the project maintainers
- 💬 **Discussions**: Use GitHub Discussions for questions
- 📚 **Documentation**: Check existing docs and ADRs

### Development Tips

- Use an IDE with Python support (VS Code with Python extension, PyCharm)
- Install a pre-commit hook for code quality checks
- Keep your fork updated with the main repository
- Test your changes thoroughly before submitting PR

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

### What This Means

You are free to:
- ✅ Use this software for any purpose
- ✅ Copy, modify, and distribute the software
- ✅ Use this software for private or commercial purposes

Under the conditions that:
- ⚠️ Include a copy of the license and copyright notice
- ⚠️ State changes made to the code

---

## Versioning

This project follows [Semantic Versioning](https://semver.org/):
- **MAJOR** - Breaking changes
- **MINOR** - New features (backward compatible)
- **PATCH** - Bug fixes (backward compatible)

Current Version: **0.0.1** (Initial Development)

---

## Acknowledgments

- Built with [FastAPI](https://fastapi.tiangolo.com/)
- Database ORM: [SQLAlchemy](https://www.sqlalchemy.org/)
- Project Author: Aniket Pendhari

---

## Support

For support, please reach out through:
- GitHub Issues: [Report a Bug](../../issues)
- GitHub Discussions: [Ask a Question](../../discussions)

---

**Last Updated**: February 2026
**Status**: Active Development
