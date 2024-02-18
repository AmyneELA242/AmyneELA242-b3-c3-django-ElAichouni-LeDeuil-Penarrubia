from django import forms
from .models import Website

class PasswordForm(forms.ModelForm):
    class Meta:
        model = Website
        fields = '__all__'
        labels = {
            'name': 'Nom du site',
            'url': 'Url du site',
            'username': 'Username',
            'password': 'Mot de passe',
        }

class CSVImportForm(forms.Form):
    csv_file = forms.FileField()