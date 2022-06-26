from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

TYPE_USER = (
    ('VENDEDOR',"Vendedor",),
    ('COMPRADOR','Comprador')
)
class SignUpForm(UserCreationForm):
    birth_date = forms.DateField(help_text='Required. Format: YYYY-MM-DD')
    type = forms.Select(choices=TYPE_USER)

    class Meta:
        model = User
        fields = ('username', 'birth_date', 'password1', 'password2', )