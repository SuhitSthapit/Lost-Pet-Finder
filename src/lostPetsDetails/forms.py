from django import forms

class SubmitAssign(forms.Form):
    url = forms.URLField()