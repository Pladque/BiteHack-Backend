from django import forms


class NewQuestion(forms.Form):
    title = forms.CharField(max_length=200)
    question = forms.CharField(label='Question', widget=forms.Textarea(), max_length=3000)
    tags = forms.CharField(label='Tags', max_length='150')

class AddSkill(forms.Form):
    skill = forms.CharField(max_length=50)

