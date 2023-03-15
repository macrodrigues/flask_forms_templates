"""Script with the class for the Python Classes Form."""
import json
import os
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms import TextAreaField, SelectField, SelectMultipleField, widgets
from wtforms.validators import Regexp, DataRequired

PATH = os.path.abspath(os.path.dirname(__file__))


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
            'Santo Amaro',
            'Valencia de Alcántara',
            'San Vicente de Alcántara',
            'La Codosera',
            'Albuquerque',
            'Other/Outro/Otro']
FREGUESIAS.sort()
EMAIL_REGEX = "(^$|^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$)"

# CHECKBOX
class MultiCheckboxField(SelectMultipleField):
    widget = widgets.ListWidget(prefix_label=False)
    option_widget = widgets.CheckboxInput()


# READ FROM JSON
with open(f"{PATH}/data/options.json") as json_file:
    data = json.load(json_file)


class PythonClassesForm(FlaskForm):
    """Class to launch Flask Form concerning Python Classes."""

    purpose = MultiCheckboxField(
        '1. Why would you like to learn Python?',
        choices=[
            data["purpose"]["Work"][0],
            data["purpose"]['Personal Projects'][0],
            data["purpose"]['Curiosity'][0],
            data["purpose"]['Other'][0]],
        validators=[
            DataRequired(message="At least one option must be selected")])
    purpose_pt = MultiCheckboxField(
        '1. Com que objectivo gostarias de aprender Python?',
        choices=[
            data["purpose"]["Work"][1],
            data["purpose"]['Personal Projects'][1],
            data["purpose"]['Curiosity'][1],
            data["purpose"]['Other'][1]])
    purpose_es = MultiCheckboxField(
        '1. ¿Con qué finalidad quieres aprender Python?',
        choices=[
            data["purpose"]["Work"][2],
            data["purpose"]['Personal Projects'][2],
            data["purpose"]['Curiosity'][2],
            data["purpose"]['Other'][2]])

    purpose_other = TextAreaField(
        "1.1. Please explain, in case you chose 'Other'.")

    purpose_other_pt = TextAreaField(
        "1.1. Explica no caso de teres escolhido 'Outro'.")

    purpose_other_es = TextAreaField(
        "1.1. Explica si has elegido 'Otro'.")

    hours_per_week = MultiCheckboxField(
        '2. How many hours a week would you like to have classes?',
        choices=['1h - 2h', '2h - 3h', '3h - 4h', '4h +'])

    hours_per_week_pt = MultiCheckboxField(
        '2. Quantas horas por semana gostarias de ter aulas?',
        choices=['1h - 2h', '2h - 3h', '3h - 4h', '4h +'])

    hours_per_week_es = MultiCheckboxField(
        '2. ¿Cuántas horas a la semana te gustaría tener clases?',
        choices=['1h - 2h', '2h - 3h', '3h - 4h', '4h +'])

    site_remote = MultiCheckboxField(
        '3. Would You rather have on-site classes or remotely?',
        choices=[
            data["site_remote"]["Remote"][0],
            data["site_remote"]["On-site"][0]])

    site_remote_pt = MultiCheckboxField(
        '3. Preferirias ter aulas à distância ou presenciais?',
        choices=[
            data["site_remote"]["Remote"][1],
            data["site_remote"]["On-site"][1]])

    site_remote_es = MultiCheckboxField(
        '3. ¿Preferirías recibir clases a distancia o presenciales?',
        choices=[
            data["site_remote"]["Remote"][1],
            data["site_remote"]["On-site"][1]])

    distance_onsite = MultiCheckboxField(
        """3.1. If you chose 'on-site', 
        how many km would you be willing to do?""",
        choices=['0 - 5km', '0 - 10km', '0 - 20km'])

    distance_onsite_pt = MultiCheckboxField(
        """3.1. Se escolheste 'presencial', quantos km estarias disposto(a) 
        a percorrer?""",
        choices=['0 - 5km', '0 - 10km', '0 - 20km'])

    distance_onsite_es = MultiCheckboxField(
        """3.1. Si has eligido 'presencial', ¿cuantos kilómetros 
        estarías dispuesto(a) a hacer?""",
        choices=['0 - 5km', '0 - 10km', '0 - 20km'])

    subject = MultiCheckboxField(
        "4. Which subject would you prefer to master with Python?",
        choices=[
            data["subject"]["Python basics"][0],
            data["subject"]["GUI's (Graphic User Interface) development"][0],
            data["subject"]["Data Analysis"][0],
            data["subject"]["Web Development"][0],
            data["subject"]["Other"][0]])

    subject_pt = MultiCheckboxField(
        "4. Quais os temas que gostarias de aprofundar com Python?",
        choices=[
            data["subject"]["Python basics"][1],
            data["subject"]["GUI's (Graphic User Interface) development"][1],
            data["subject"]["Data Analysis"][1],
            data["subject"]["Web Development"][0],
            data["subject"]["Other"][1]])

    subject_es = MultiCheckboxField(
        "4. ¿Qué temas te gustaría profundizar con Python?",
        choices=[
            data["subject"]["Python basics"][1],
            data["subject"]["GUI's (Graphic User Interface) development"][2],
            data["subject"]["Data Analysis"][2],
            data["subject"]["Web Development"][1],
            data["subject"]["Other"][2]])

    subject_other = TextAreaField(
        "4.1. Please explain, in case you chose 'Other'.")

    subject_other_pt = TextAreaField(
        "4.1. Explica no caso de teres escolhido 'Outro'.")

    subject_other_es = TextAreaField(
        "4.1. Explica si has elegido 'Otro'.")

    pay = SelectField(
        "5. Would You be willing to pay for having classes?",
        choices=[
            data["pay"]["Yes"][0],
            data["pay"]["No"][0]])

    pay_pt = SelectField(
        "5. Estarias disposto(a) a pagar para frequentar as aulas?",
        choices=[
            data["pay"]["Yes"][1],
            data["pay"]["No"][1]])

    pay_es = SelectField(
        "5. ¿Estarías dispuesto(a) a pagar por asistir a clases?",
        choices=[
            data["pay"]["Yes"][2],
            data["pay"]["No"][2]])

    pay_how_much = MultiCheckboxField(
        "5.1. If 'Yes', how much would you be willing to pay?",
        choices=[
            data["pay_how_much"]["8 - 15€ per week"][0],
            data["pay_how_much"]["20 - 30€ per month"][0],
            data["pay_how_much"]["30 - 40€ per month"][0],
            data["pay_how_much"]["5 - 10€ per session (1-2 hours)"][0],
            data["pay_how_much"]["Other"][0]])

    pay_how_much_pt = MultiCheckboxField(
        "5.1. Se 'sim', quanto é que estarias disposto(a) a pagar?",
        choices=[
            data["pay_how_much"]["8 - 15€ per week"][1],
            data["pay_how_much"]["20 - 30€ per month"][1],
            data["pay_how_much"]["30 - 40€ per month"][1],
            data["pay_how_much"]["5 - 10€ per session (1-2 hours)"][1],
            data["pay_how_much"]["Other"][1]])

    pay_how_much_es = MultiCheckboxField(
        "5.1. Si sí, ¿cuánto estarías dispuesto(a) a pagar?",
        choices=[
            data["pay_how_much"]["8 - 15€ per week"][2],
            data["pay_how_much"]["20 - 30€ per month"][2],
            data["pay_how_much"]["30 - 40€ per month"][2],
            data["pay_how_much"]["5 - 10€ per session (1-2 hours)"][2],
            data["pay_how_much"]["Other"][2]])

    pay_how_much_other = TextAreaField(
        "5.2. Please explain, in case you chose 'Other'.")

    pay_how_much_other_pt = TextAreaField(
        "5.2. Explica no caso de teres escolhido 'Outro'.")

    pay_how_much_other_es = TextAreaField(
        "5.2. Explica si has elegido 'Otro'.")

    pay_premium = SelectField(
        """5.3. Would you be willing to pay a premium subscription,
          for extra classes and customized support to build a portfolio?""",
        choices=[
            data["pay_premium"]["Yes"][0],
            data["pay_premium"]["No"][0],
            data["pay_premium"]["Maybe"][0]])

    pay_premium_pt = SelectField(
        """5.3. Estarias disposto(a) a pagar uma subscrição premium
        para ter aulas extra e apoio personalizado para 
        construir um portfólio?""",
        choices=[
            data["pay_premium"]["Yes"][1],
            data["pay_premium"]["No"][1],
            data["pay_premium"]["Maybe"][1]])

    pay_premium_es = SelectField(
        """5.3. ¿Estarías dispuesto(a) a pagar una suscripción premium
        para tener clases extra y apoyo personalizado para construir 
        un portafolio?""",
        choices=[
            data["pay_premium"]["Yes"][2],
            data["pay_premium"]["No"][2],
            data["pay_premium"]["Maybe"][2]])

    when = MultiCheckboxField(
        "6. When you rather have the classes?",
        choices=[
            data["when"]["During the week"][0],
            data["when"]["Weekends"][0]])

    when_pt = MultiCheckboxField(
        "6. Quando gostavas de ter aulas?",
        choices=[
            data["when"]["During the week"][1],
            data["when"]["Weekends"][1]])

    when_es = MultiCheckboxField(
        "6. ¿Cuándo te gustaría tener las clases?",
        choices=[
            data["when"]["During the week"][2],
            data["when"]["Weekends"][2]])

    when_hours = MultiCheckboxField(
        "6.1. At what time of the day?",
        choices=[
            data["when_hours"]["Morning"][0],
            data["when_hours"]["Afternoon"][0],
            data["when_hours"]["Evening"][0]])

    when_hours_pt = MultiCheckboxField(
        "6.1. Em que altura do dia?",
        choices=[
            data["when_hours"]["Morning"][1],
            data["when_hours"]["Afternoon"][1],
            data["when_hours"]["Evening"][1]])

    when_hours_es = MultiCheckboxField(
        "6.1. ¿En qué momento del día?",
        choices=[
            data["when_hours"]["Morning"][2],
            data["when_hours"]["Afternoon"][2],
            data["when_hours"]["Evening"][2]])

    age = StringField("7. Can you please provide your age?")

    age_pt = StringField("7. Qual é a tua idade?")

    age_es = StringField("7. ¿Cuántos años tienes?")

    location = SelectField(
        "8. Can you please provide your location?",
        choices=FREGUESIAS)

    location_pt = SelectField(
        "8. Qual é a tua localização?",
        choices=FREGUESIAS)

    location_es = SelectField(
        "8. ¿Cuál es tu ubicación?",
        choices=FREGUESIAS)

    email = StringField(
        """9. If you would like to be contacted for more 
        information, please provide your email address.""",
        validators=[
            Regexp(
                EMAIL_REGEX,
                message='Please provide a valid email address.')])

    email_pt = StringField(
        """9. Se gostarias de ser contactado(a) para mais informações,
        por favor deixa aqui o teu email.""",
        validators=[
            Regexp(
                EMAIL_REGEX,
                message='Este email não é válido.')])

    email_es = StringField(
        """9. Si deseas ser contactado(a) para más
        informaciones, deja aquí tu email.""",
        validators=[
            Regexp(
                EMAIL_REGEX,
                message='Please provide a valid email address.')])

    observations = TextAreaField("10. Please write below any observations.")

    observations_pt = TextAreaField("10. Deixa alguma nota adicional.")

    observations_es = TextAreaField("10. Escribe cualquier observación.")

    submit = SubmitField('Submit')
    submit_pt = SubmitField('Enviar')
    submit_es = SubmitField('Enviar')
