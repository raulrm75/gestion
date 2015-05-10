from django import forms
from django.forms import ModelForm
from centro.models import Cursos

class UnidadForm(forms.Form):
	Unidad = forms.ModelChoiceField(queryset=Cursos.objects.order_by('Curso'), empty_label=None)