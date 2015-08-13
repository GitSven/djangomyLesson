#-*-coding:utf-8-*-
from django import forms

class Addform(forms.Form):

    a = forms.FloatField()
    b = forms.FloatField()

