from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SubmitField, DateField, DateTimeField
from wtforms import TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp


class ServicesForm(FlaskForm):
    """Class to launch Flask Form concerning consultory services."""

    pass
