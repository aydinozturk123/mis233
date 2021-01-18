from django import forms

class SurveyForm(forms.Form):
    question1 = forms.CharField(label='question1', max_length=100)
    question2 = forms.CharField(label='question2', max_length=100)
    question3 = forms.CharField(label='question3', max_length=100)
    question4 = forms.CharField(label='question4', max_length=100)
    question5 = forms.CharField(label='question5', max_length=100)
    question6 = forms.CharField(label='question6', max_length=100)
    question7 = forms.CharField(label='question7', max_length=100)
    question8 = forms.CharField(label='question8', max_length=100)
    question9 = forms.CharField(label='question9', max_length=100)
    question10 = forms.CharField(label='question10', max_length=100)
    question11 = forms.CharField(label='question11', max_length=100)
    question12 = forms.CharField(label='question12', max_length=100)