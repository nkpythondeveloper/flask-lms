# lms/forms/auth.py
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class LoginForm(FlaskForm):
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=255)],
        render_kw={"placeholder": "user@example.com"}
    )
    password = PasswordField(
        "Password",
        validators=[DataRequired(), Length(min=6, max=128)],
        render_kw={"placeholder": "Enter your password"}
    )
    submit = SubmitField("Sign in")

class AdminCreateUserForm(FlaskForm):
    first_name = StringField(
        "First name",
        validators=[DataRequired(), Length(max=80)],
        render_kw={"placeholder": "John"}
    )
    last_name = StringField(
        "Last name",
        validators=[Length(max=80)],
        render_kw={"placeholder": "Doe"}
    )
    email = StringField(
        "Email",
        validators=[DataRequired(), Email(), Length(max=255)],
        render_kw={"placeholder": "librarian@example.com"}
    )
    password = PasswordField(
        "Temp password",
        validators=[DataRequired(), Length(min=8, max=128)],
        render_kw={"placeholder": "Temporary password"}
    )
    role_id = SelectField(
        "Role",
        coerce=int,
        validators=[DataRequired()],
        render_kw={"placeholder": "Select role"}
    )
    submit = SubmitField("Create user")