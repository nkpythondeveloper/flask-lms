# lms/models/user.py
from datetime import datetime, timezone
from flask_login import UserMixin
from ..extensions import db, bcrypt

class Role(db.Model):
    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True, nullable=False)  # "admin" | "librarian" | "member"

    def __repr__(self) -> str: # pragma: no cover
        return f"<Role {self.name}>"

class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)

    email = db.Column(db.String(255), unique=True, index=True, nullable=False)

    first_name = db.Column(db.String(80), nullable=False)
    last_name  = db.Column(db.String(80), nullable=True)

    password_hash = db.Column(db.String(255), nullable=False)

    role_id = db.Column(db.Integer, db.ForeignKey("roles.id"), index=True)
    role    = db.relationship(Role)

    active     = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.now(timezone.utc))

    
    def set_password(self, raw: str) -> None:
        self.password_hash = bcrypt.generate_password_hash(raw).decode("utf-8")

    def check_password(self, raw: str) -> bool:
        return bcrypt.check_password_hash(self.password_hash, raw)

    @property
    def full_name(self) -> str:
        return f"{self.first_name} {self.last_name or ''}".strip()

    @property
    def is_admin(self) -> bool:
        return bool(self.role and self.role.name == "admin")

    def __repr__(self) -> str: # pragma: no cover
        return f"<User {self.email} ({self.full_name})>"