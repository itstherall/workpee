from dataclasses import fields
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from login.models import Loja, Pedido, Produto

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


class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'descricao', 'imagem', 'loja']


ProdutoFormSet = forms.inlineformset_factory(
    Loja,
    Produto,
    extra=0,
    validate_max=True,
    min_num=1,
    max_num=1,
    form=ProdutoForm,
)


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['quantidade', 'customizacao']


PedidoFormSet = forms.inlineformset_factory(
    Produto,
    Pedido,
    extra=0,
    validate_max=True,
    min_num=1,
    max_num=1,
    form=PedidoForm,
)
