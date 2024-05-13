from django import forms
from Employe.models import employess


class Employeeform(forms.ModelForm):
    class Meta:
        model=employess
        fields='__all__'