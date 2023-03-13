from flask_wtf import FlaskForm
from wtforms import widgets, StringField, SubmitField, DateField, DateTimeField
from wtforms import TextAreaField, SelectField, BooleanField
from wtforms.validators import DataRequired, Email, Length, Regexp


class PythonClassesForm(FlaskForm):
    """Class to launch Flask Form concerning Python Classes."""
    purpose = SelectField(
        'Why would you like to learn Python?',
        choices=[
            'Work',
            'Personal projects',
            'Curiosity',
            'Other'
        ],
        validators=[DataRequired(message='Please select an option.')])

    purpose_other = StringField("Please explain, in case you chose 'Other'.")

    hours_per_week = SelectField(
        'How many hours a week would you like to have classes?',
        choices=[
            '1h - 2h',
            '2h - 3h',
            '3h - 4h',
            '4h +'
        ],
        validators=[DataRequired(message='Please select an option.')])
    
    site_remote = SelectField(
        'Would You rather have on-site classes or remotely?',
        choices=[
            'On-site',
            'Remote',
            'No preference'
        ],
        validators=[DataRequired(message='Please select an option.')])
    
    distance_onsite = SelectField(
        """If you chose 'on-site', how many km would you be willing to do,
          to attend the classes?""",
        choices=[
            '0k-5km',
            '0k-10km',
            '0k-20km'
        ])