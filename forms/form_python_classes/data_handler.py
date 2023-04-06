# -*- coding: utf-8 -*-

"""Script to read and write the data from the forms into .csv files."""
import os
import pandas as pd
from .form_python_classes import PythonClassesForm
from .form_python_classes import PythonClassesFormPT
from .form_python_classes import PythonClassesFormES

# PATHS
PATH = os.path.abspath(os.path.dirname(__file__))
OUTPUT = f"{PATH}/data/output_python_classes.csv"


headers = [
    'Purpose',
    'Purpose (Other)',
    'Hours (p/week)',
    'On-site/Remote',
    'Distance',
    'Subject',
    'Subject (Other)',
    'Pay',
    'How much',
    'How much (Other)',
    'Premium',
    'When',
    'Time of the day',
    'Age',
    'Location',
    'Email',
    'Observations']


def write_data(lang):
    """Write data gathered from the english form."""
    forms_per_lang = {
        'en': PythonClassesForm(),
        'pt': PythonClassesFormPT(),
        'es': PythonClassesFormES()}
    form = forms_per_lang[lang]
    fields = {}
    for field in form:
        fields[field.name] = field.data
    values_transf = []
    values = list(fields.values())[:-2]
    for val in values:
        if type(val) == list:
            val = ', '.join(val)
            values_transf.append(val)
        else:
            values_transf.append(val)
    fields = dict(zip(headers, values_transf))
    df = pd.DataFrame(fields, index=[0])
    df.to_csv(OUTPUT, encoding='utf-16')
