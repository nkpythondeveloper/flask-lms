from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, Optional

class CategoryForm(FlaskForm):
    name = StringField(
        "Category name",
        validators=[DataRequired(), Length(max=80)],
        render_kw={"placeholder": "e.g., Fiction, Science, History"}
    )
    submit = SubmitField("Save category")

class BookForm(FlaskForm):
    title = StringField(
        "Title",
        validators=[DataRequired(), Length(max=255)],
        render_kw={"placeholder": "Book title"}
    )
    isbn = StringField(
        "ISBN",
        validators=[Optional(), Length(max=20)],
        render_kw={"placeholder": "978-3-16-148410-0"}
    )
    description = TextAreaField(
        "Description",
        validators=[Optional(), Length(max=5000)],
        render_kw={"placeholder": "Brief description of the book"}
    )
    category_id = SelectField(
        "Category",
        coerce=int,
        validators=[Optional()],
        render_kw={"placeholder": "Select category"}
    )
    authors_csv = StringField(
        "Authors (comma-separated)",
        validators=[Optional(), Length(max=512)],
        render_kw={"placeholder": "e.g., J.K. Rowling, Neil Gaiman"}
    )
    tags_csv = StringField(
        "Tags (comma-separated)",
        validators=[Optional(), Length(max=512)],
        render_kw={"placeholder": "e.g., fantasy, adventure, kids"}
    )
    submit = SubmitField("Save book")

class BookCopyForm(FlaskForm):
    book_id = SelectField(
        "Book",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Select book"}
    )
    barcode = StringField(
        "Barcode (leave empty to auto-generate)",
        validators=[Optional(), Length(max=64)],
        render_kw={"placeholder": "Auto-generated if left blank"}
    )
    submit = SubmitField("Add copy")