"""Launch the templates on a Flask server."""
import os
import datetime as dt
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_recaptcha import ReCaptcha
from flask_mail import Mail, Message
from forms.form_python_classes.form_python_classes import PythonClassesForm
from forms.form_python_classes.form_python_classes import PythonClassesFormPT
from forms.form_python_classes.form_python_classes import PythonClassesFormES
from forms.form_python_classes.data_handler import write_data

# import dotenv
# dotenv.load_dotenv('keys.env')

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY')   # You can use a random key
# app.config['UPLOAD_FOLDER'] = os.path.dirname(
#     os.path.abspath(__file__))  # to add attachments
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv("MAIL")
app.config['MAIL_PASSWORD'] = os.getenv("PASS")
app.config['MAIL_USE_TLS'] = True  # more secure version of SSL.
app.config['MAIL_USE_SSL'] = False
app.config['RECAPTCHA_SITE_KEY'] = os.getenv('key_site')
app.config['RECAPTCHA_SECRET_KEY'] = os.getenv('key_secret')
recaptcha = ReCaptcha(app)
mail = Mail(app)
Bootstrap(app)


def send_email_results():
    """Send email with all the inputs."""
    msg = Message(
        "Python Classes",
        sender='mac.rodrigues@outlook.com',
        recipients=['mac.rodrigues@outlook.com'])
    file = 'forms/form_python_classes/data/output_python_classes.csv'
    with app.open_resource(file) as fp:
        msg.attach('python_classes_results.csv', "text/csv", data=fp.read())

    # send email
    mail.send(msg)


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
