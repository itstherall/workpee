from random import choice
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

TYPE_USER = (
    ('VENDEDOR', "Vendedor",),
    ('COMPRADOR', 'Comprador')
)


class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Email'}))
    username = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Usuário'}))
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "usuário"
        self.fields['password1'].label = "Senha"
        self.fields['password2'].label = "Confirmar Senha"

        self.fields['username'].help_text = None
        self.fields['password1'].help_text = None
        self.fields['password2'].help_text = None

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
