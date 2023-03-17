"""Script to read and write the data from the forms into csv files."""
import os
import pandas as pd
from .form_python_classes import PythonClassesForm
from .form_python_classes import PythonClassesFormPT
from .form_python_classes import PythonClassesFormES

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

def write_data_en():
    form = PythonClassesForm()
    fields = {}
    for field in form:
        fields[field.name] = field.data
    fields = dict(zip(headers, list(fields.values())[:-2]))
    df = pd.DataFrame.from_dict(fields)
    df.to_csv(OUTPUT)