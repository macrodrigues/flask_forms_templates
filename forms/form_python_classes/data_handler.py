from .form_python_classes import PythonClassesForm

def write_data():
    form = PythonClassesForm()
    fields = {}
    for field in form:
        fields[field.name] = field.data
    print(fields)