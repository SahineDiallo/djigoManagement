from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["email", "first_name", "last_name",
                  "username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.fields['email'].label = "Addresse Mail"
        self.fields['password1'].label = "Mot de passe"
        self.fields['password2'].label = "Confirmer"
        self.fields['username'].label = "Nom d'utilisateur"
        self.fields['first_name'].label = "Prenom"
        self.fields['last_name'].label = "Nom de famille"
        self.fields['email'].required = True
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-6 mb-2'),
                Column('last_name', css_class='form-group col-md-6 mb-2'),
                css_class='row'
            ),
            'email',
            'username',
            "password1",
            "password2",
            # CustomCheckbox('check_me_out'),w  # <-- Here
            Submit('submit', 'Creer compte',
                   css_class="btn btn-secondary btn-sm")
        )

