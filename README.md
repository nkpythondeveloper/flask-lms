# Library Management System (Flask + Celery + Redis)

A role-based Library Management System built with Flask, SQLAlchemy, Celery, Redis, and Docker.

### Features (Planned)
- User authentication & roles (Admin, Librarian, Member)
- Book catalog with search & CRUD
- Borrow, return, renew workflows
- Overdue fine calculation
- Email notifications with Celery & Redis
- Reports & analytics dashboard

### Tech Stack
- **Backend**: Flask, SQLAlchemy, Flask-Migrate, Flask-Login
- **Tasks**: Celery + Redis
- **UI**: HTML, CSS (Tailwind planned)
- **Deployment**: Docker, Gunicorn