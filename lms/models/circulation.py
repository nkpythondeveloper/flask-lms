from datetime import datetime
from ..extensions import db

class Loan(db.Model):
    __tablename__ = "loans"
    id = db.Column(db.Integer, primary_key=True)

    copy_id = db.Column(db.Integer, db.ForeignKey("book_copies.id"), nullable=False, index=True)
    member_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    issued_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    due_at = db.Column(db.DateTime, nullable=False, index=True)
    returned_at = db.Column(db.DateTime, nullable=True)

    # Relationships
    copy = db.relationship("BookCopy", backref="loans")
    member = db.relationship("User", backref="loans")

    def __repr__(self):  # pragma: no cover
        return f"<Loan copy={self.copy_id} member={self.member_id} due={self.due_at}>"

class Reservation(db.Model):
    __tablename__ = "reservations"
    id = db.Column(db.Integer, primary_key=True)

    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False, index=True)
    member_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False, index=True)

    status = db.Column(db.String(20), default="active", nullable=False)  # active|fulfilled|cancelled
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    # Relationships
    book = db.relationship("Book", backref="reservations")
    member = db.relationship("User", backref="reservations")

    def __repr__(self):  # pragma: no cover
        return f"<Reservation book={self.book_id} member={self.member_id} status={self.status}>"

class Fine(db.Model):
    __tablename__ = "fines"
    id = db.Column(db.Integer, primary_key=True)

    loan_id = db.Column(db.Integer, db.ForeignKey("loans.id"), nullable=False, index=True)
    amount = db.Column(db.Numeric(8, 2), nullable=False)
    settled = db.Column(db.Boolean, default=False, nullable=False)

    # Relationships
    loan = db.relationship("Loan", backref="fines")

    def __repr__(self):  # pragma: no cover
        return f"<Fine loan={self.loan_id} amount={self.amount} settled={self.settled}>"