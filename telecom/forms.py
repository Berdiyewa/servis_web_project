from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput, Select
from .models import TelecomData

class TelecomDataForm(ModelForm):
    class Meta:
        model = TelecomData
        fields = ['hyzmat', 'sahs', 'ady', 'salgy', 'mobil_belgi', 'telefon_belgi', 'mesele', 'sene']

        widgets = {
            "hyzmat": Select(choices=[('wifi', 'Wifi'), ('ip', 'IP')], attrs={'class': 'form-control'}),
            "sahs": Select(choices=[('Fiziki', 'Fiziki'), ('Ýuridiki', 'Ýuridiki'), ('Başga', 'Başga')], attrs={'class': 'form-control'}),
            "ady": TextInput(attrs={'class': 'form-control', 'placeholder': 'Ady, familiýasy'}),
            "salgy": TextInput(attrs={'class': 'form-control', 'placeholder': 'Öý salgyňyz'}),
            "mobil_belgi": TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon belgiňiz'}),
            "telefon_belgi": TextInput(attrs={'class': 'form-control', 'placeholder': 'Öý telefon belgiňiz'}),
            "mesele": Textarea(attrs={'class': 'form-control', 'placeholder': 'Meseläňiz', 'style':'border-radius: 7px'}),
            "sene": DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Wagty saýlaň', 'type': 'datetime-local'}),
        }