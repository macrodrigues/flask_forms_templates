import os
import datetime as dt
from flask import Flask, render_template, flash
from flask_bootstrap import Bootstrap
from flask_mail import Mail
# from flask_mail import Message
from forms.form_python_classes.form_python_classes import PythonClassesForm
from forms.form_photography.form_photography import PhotographyForm
from forms.form_services.form_services import ServicesForm


app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = os.path.dirname(os.path.abspath(__file__)) # to add attachments
app.config['MAIL_SERVER'] = os.getenv("MAIL_SERVER")
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = os.getenv("MAIL_USERNAME")
app.config['MAIL_PASSWORD'] = os.getenv("PASS")
app.config['MAIL_USE_TLS'] = True  # more secure version of SSL.
app.config['MAIL_USE_SSL'] = False

mail = Mail(app)
Bootstrap(app)


def send_email_results():
    """Send email with all the inputs."""
    pass


def render_page(lang, html):
    """Render page. Takes the language and html file as inputs."""
    current_year = dt.datetime.now().year
    if form.is_submitted():  # if form is submitted
        if form.validate():  # if form is validated
            send_email_results()
            if lang == "pt":
                return render_template("success_pt.html")
            if lang == "en":
                return render_template("success_en.html")
            if lang == "es":
                return render_template("success_es.html")
        else:
            if lang == "pt":
                flash('*Alguns campos estão incompletos ou em falta.')
            if lang == "en":
                flash('*Some fields are incomplete or missing.')
            if lang == "es":
                flash('*Algunos campos están incompletos o faltan.')
    return render_template(html, year=current_year, form=form)


@app.route("/", methods=["GET", "POST"])
def home_en():
    """Render the html in english language."""
    return render_page('en', html_en)


@app.route("/pt", methods=["GET", "POST"])
def home_pt():
    """Render the html in portuguese language."""
    return render_page('pt', html_pt)


@app.route("/es", methods=["GET", "POST"])
def home_es():
    """Render the html in spanish language."""
    return render_page('es', html_es)


if __name__ == '__main__':
    # run application
    if __name__ == '__main__':
        # select form
        form = PythonClassesForm()  # here select the form you whish to use
        if form == PythonClassesForm():
            html_pt = 'index_python_pt.html'
            html_en = 'index_python_en.html'
            html_es = 'index_python_es.html'
        if form == PhotographyForm():
            html_pt = 'index_photo_pt.html'
            html_en = 'index_photo_en.html'
            html_es = 'index_photo_es.html'
        if form == ServicesForm():
            html_pt = 'index_services_pt.html'
            html_en = 'index_services_en.html'
            html_es = 'index_services_es.html'
        # run application
        app.run(port=5000)
    else:
        application = app
