from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import TextAreaField, SelectField
from wtforms.validators import DataRequired, Email, Regexp


# VARIABLES
ERROR_SELECT_OPTION = 'Please select an option.'
FREGUESIAS = [
            'Alter do Chão',
            'Chancelaria',
            'Cunheira',
            'Seda',
            'Arronches, Assunção',
            'Esperança',
            'Mosteiros',
            'Avis',
            'Ervedal',
            'Aldeia Velha',
            'Figueira e Barros',
            'Campo Maior',
            'Nossa Senhora da Graça dos Degolados',
            'São João Baptista '
            'Castelo de Vide',
            'Póvoa e Meadas',
            'Santa Maria da Devesa',
            'Santiago Maior',
            'São João Baptista',
            'Crato e Mártires',
            'Aldeia da Mata',
            'Gáfete',
            'Monte da Pedra',
            'Elvas',
            'Santa Eulália',
            'São Brás e São Lourenço',
            'São Vicente e Ventosa',
            'Fronteira',
            'Cabeço de Vide',
            'São Saturnino',
            'Gavião',
            'Belver',
            'Comenda',
            'Margem',
            'Marvão',
            'Beirã',
            'Santo António das Areias',
            'São Salvador da Aramenha',
            'Monforte',
            'Assumar',
            'Santo Aleixo',
            'Vaiamonte', 
            'Nisa', 
            'Alpalhão',
            'Montalvão',
            'Santana',
            'São Matias',
            'Tolosa',
            'Ponte de Sor',
            'Foros de Arrão',
            'Galveias',
            'Longomel',
            'Montargil',
            'Portalegre',
            'Alagoa',
            'Fortios',
            'Sousel',
            'Cano',
            'Casa Branca',
            'Santo Amaro']
FREGUESIAS.sort()
EMAIL_REGEX = "(^$|^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"

class PythonClassesForm(FlaskForm):
    """Class to launch Flask Form concerning Python Classes."""

    purpose = SelectField(
        '1. Why would you like to learn Python?',
        choices=['Work', 'Personal projects', 'Curiosity', 'Other'])

    purpose_other = StringField(
        "1.1. Please explain, in case you chose 'Other'.")

    hours_per_week = SelectField(
        '2. How many hours a week would you like to have classes?',
        choices=['1h - 2h', '2h - 3h', '3h - 4h', '4h +'])

    site_remote = SelectField(
        '3. Would You rather have on-site classes or remotely?',
        choices=['On-site', 'Remote', 'No preference'])

    distance_onsite = SelectField(
        """3.1. If you chose 'on-site', 
        how many km would you be willing to do?""",
        choices=['0k-5km', '0k-10km', '0k-20km'])

    subject = SelectField(
        "4. Which subject would you prefer to master with Python?",
        choices=[
            'Python basics',
            "GUI's (Graphic User Interface) development",
            'Data Anlaysis',
            'Web Development',
            'Other'
        ])

    subject_other = StringField(
        "4.1. Please explain, in case you chose 'Other'.")

    pay = SelectField(
        "5. Would You be willing to pay for having classes?",
        choices=['Yes', 'No'])
    
    pay_how_much = SelectField(
        "5.1. If 'Yes', how much would you be willing to pay?",
        choices=[
            '8-15€ per week',
            '20-30€ per month',
            '30-40€ per month',
            '5-10€ per session (1-2 hours)',
            'Other'
        ])

    pay_how_much_other = StringField(
        "5.2. Please explain, if you chose 'Other' type of payment.")

    pay_premium = SelectField(
        """5.3. Would you be willing to pay a premium subscription,
          for extra classes and customized support to build a portfolio?""",
        choices=['Yes', 'No', 'Maybe'])

    when = SelectField(
        "6. When you rather have the classes?",
        choices=['During the week', 'Weekends'])

    when_hours = SelectField(
        "6.1. At what time of the day?",
        choices=['Morning', 'Afternoon', 'Evening'])

    age = StringField("7. Can you please provide your age?")

    location = SelectField(
        "8. Can you please provide your location?",
        choices=FREGUESIAS)

    # email = StringField("9. If you would like to be contacted for more information, and be shortlisted for Python Classes, please provide your email address:",
    #     validators=[Email(message='Please insert a valid email.')])

    email = StringField(
        """9. If you would like to be contacted for more 
        information, please provide your email address.""",
        validators=[
            Regexp(
                EMAIL_REGEX,
                message='Please provide a valid email address.')])
    
    observations = TextAreaField("Please write below any observations:")

    submit = SubmitField('Submit')
