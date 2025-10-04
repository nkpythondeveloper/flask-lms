from ..extensions import db

# Association table for many-to-many Book<->Author
book_authors = db.Table(
    "book_authors",
    db.Column("book_id", db.Integer, db.ForeignKey("books.id"), primary_key=True),
    db.Column("author_id", db.Integer, db.ForeignKey("authors.id"), primary_key=True),
)

class Author(db.Model):
    __tablename__ = "authors"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), index=True, nullable=False)

    # Backref gives us: author.books
    def __repr__(self):  # pragma: no cover
        return f"<Author {self.name}>"

class Category(db.Model):
    __tablename__ = "categories"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, index=True, nullable=False)

    # Relationship: one category → many books
    books = db.relationship("Book", backref="category", lazy="dynamic")

    def __repr__(self):  # pragma: no cover
        return f"<Category {self.name}>"

class Book(db.Model):
    __tablename__ = "books"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), index=True, nullable=False)
    isbn = db.Column(db.String(20), unique=True, index=True)
    description = db.Column(db.Text)

    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"))

    # Many-to-many: book.authors, author.books
    authors = db.relationship("Author", secondary=book_authors, backref="books")

    # One-to-many: book.copies
    copies = db.relationship("BookCopy", backref="book", lazy="dynamic")

    # Simple CSV string of tags (for MVP)
    tags = db.Column(db.String(255))

    def __repr__(self):  # pragma: no cover
        return f"<Book {self.title} ({self.isbn or 'no-isbn'})>"

class BookCopy(db.Model):
    __tablename__ = "book_copies"
    id = db.Column(db.Integer, primary_key=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False, index=True)

    barcode = db.Column(db.String(64), unique=True, index=True, nullable=True)
    status = db.Column(db.String(20), default="available", nullable=False)
    # available | on_loan | lost | repair

    def __repr__(self):  # pragma: no cover
        return f"<Copy {self.barcode or self.id} of Book#{self.book_id} [{self.status}]>"