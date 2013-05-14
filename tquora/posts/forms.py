from django import forms

class AddQuestionForm(forms.Form):

    topic = forms.CharField(max_length=100)
    question = forms.CharField(widget=forms.Textarea)
    detail = forms.CharField(max_length=100)
   
