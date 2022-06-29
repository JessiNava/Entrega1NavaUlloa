from django import forms

class Hobbieformulario(forms.Form):
    nombre=forms.CharField()
    horas_sem=forms.IntegerField()