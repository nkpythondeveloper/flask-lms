from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Optional, NumberRange

class IssueForm(FlaskForm):
    copy_barcode = StringField(
        "Copy barcode",
        validators=[DataRequired(), Length(max=64)],
        render_kw={"placeholder": "Scan or enter copy barcode"}
    )
    member_email = StringField(
        "Member email",
        validators=[DataRequired(), Email(), Length(max=255)],
        render_kw={"placeholder": "member@example.com"}
    )
    loan_days = IntegerField(
        "Loan days",
        validators=[Optional(), NumberRange(min=1, max=90)],
        render_kw={"placeholder": "Default per policy (optional)"}
    )
    submit = SubmitField("Issue book")

class ReturnForm(FlaskForm):
    copy_barcode = StringField(
        "Copy barcode",
        validators=[DataRequired(), Length(max=64)],
        render_kw={"placeholder": "Scan or enter copy barcode"}
    )
    submit = SubmitField("Return book")

class RenewForm(FlaskForm):
    copy_barcode = StringField(
        "Copy barcode",
        validators=[DataRequired(), Length(max=64)],
        render_kw={"placeholder": "Scan or enter copy barcode"}
    )
    extra_days = IntegerField(
        "Extend by (days)",
        validators=[DataRequired(), NumberRange(min=1, max=30)],
        render_kw={"placeholder": "Number of days to extend"}
    )
    submit = SubmitField("Renew loan")

class ReservationForm(FlaskForm):
    book_id = IntegerField(
        "Book ID",
        validators=[DataRequired(), NumberRange(min=1)],
        render_kw={"placeholder": "Enter book ID to reserve"}
    )
    member_email = StringField(
        "Member email",
        validators=[DataRequired(), Email(), Length(max=255)],
        render_kw={"placeholder": "member@example.com"}
    )
    submit = SubmitField("Reserve book")