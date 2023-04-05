"""Launch the templates on a Flask server."""
import os
import datetime as dt
import smtplib
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from forms.form_python_classes.form_python_classes import PythonClassesForm
from forms.form_python_classes.form_python_classes import PythonClassesFormPT
from forms.form_python_classes.form_python_classes import PythonClassesFormES
from forms.form_python_classes.data_handler import write_data

# import dotenv
# dotenv.load_dotenv('keys.env')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY') # You can use a random key
Bootstrap(app)

OWN_EMAIL = os.getenv('MAIL')
OWN_PASSWORD = os.getenv('PASS')


def send_email_results():
    """Send email with all the inputs."""
    email_message = "Hey"
    msg = MIMEMultipart()
    msg['To'] = OWN_EMAIL
    msg['Subject'] = 'Python Classes'
    msg.attach(MIMEText(email_message, "plain"))
    text = msg.as_string()
    with smtplib.SMTP(host='smtp-mail.outlook.com', port=587) as connection:
        connection.starttls()
        connection.login(OWN_EMAIL, OWN_PASSWORD)
        connection.sendmail(OWN_EMAIL, OWN_EMAIL, text)



def render_page(lang, html):
    """Render page. Takes the language and html file as inputs."""
    forms_per_lang = {
        'en': PythonClassesForm(),
        'pt': PythonClassesFormPT(),
        'es': PythonClassesFormES()}
    lang_dict = {
        'pt': "success_pt.html",
        'en': "success_en.html",
        'es': "success_es.html"}
    lang_error_dict = {
        'pt': "Alguns campos estão incompletos ou em falta.",
        'en': "Some fields are incomplete or missing.",
        'es': "Algunos campos están incompletos o faltan."}
    form = forms_per_lang[lang]
    current_year = dt.datetime.now().year
    if form.is_submitted():  # if form is submitted
        if form.validate():  # if form is validated
            write_data(lang)
            send_email_results()
            return render_template(lang_dict[lang])
        else:
            flash(lang_error_dict[lang])
    return render_template(html, language=lang, year=current_year, form=form)


@app.route("/", methods=["GET", "POST"])
def home_en():
    """Render the html in english language."""
    return render_page('en', 'index_python_en.html')


@app.route("/pt", methods=["GET", "POST"])
def home_pt():
    """Render the html in portuguese language."""
    return render_page('pt', 'index_python_pt.html')


@app.route("/es", methods=["GET", "POST"])
def home_es():
    """Render the html in spanish language."""
    return render_page('es', 'index_python_es.html')


if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)
