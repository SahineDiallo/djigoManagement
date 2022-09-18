from django import forms
from .models import Patient
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        fields = ["prenom", "nom", "age", "adresse", "numero_de_telephone",
                  "genre", "prescriptions", "observations", ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('prenom', css_class='form-group col-md-6 mb-2'),
                Column('nom', css_class='form-group col-md-6 mb-2'),
                css_class='row'
            ),
            Row(
                Column('age', css_class='form-group col-md-3 mb-2'),
                Column('adresse', css_class='form-group col-md-9 mb-2'),
                css_class='row'
            ),
            Row(
                Column('numero_de_telephone',
                       css_class='form-group col-md-9 mb-2'),
                Column('genre', css_class='form-group col-md-3 mb-2'),
                css_class='row'
            ),
            "prescriptions",
            "observations",

            # CustomCheckbox('check_me_out'),w  # <-- Here
            Submit('submit', 'Ajouter Patient',
                   css_class="btn btn-success")
        )
