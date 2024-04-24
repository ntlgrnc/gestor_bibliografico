from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label='Correo electrónico', max_length=254, help_text='Asegúrate de ingresar un correo electrónico válido.', required=True)
    first_name = forms.CharField(label='Nombres', max_length=30, required=True)
    last_name = forms.CharField(label='Apellidos', max_length=30, required=True)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput, help_text=None, required=True)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput, help_text=None, required=True)

    field_order = ['first_name', 'last_name', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Eliminar el campo de nombre de usuario
        self.fields.pop('username')

    def save(self, commit=True):
        user = super().save(commit=False)
        # Establecer el nombre de usuario como el correo electrónico
        user.username = self.cleaned_data['email']
        if commit:
            user.save()
        return user
