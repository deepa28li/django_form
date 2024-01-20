from django import forms

g=[['MALE','MALE'],['FEMALE','FEMALE']]
c=[['PYTHON','PYTHON'],['SQL','SQL'],['Django','DJANGO']]
class NameForm(forms.Form):
    sname=forms.CharField()
    sage=forms.IntegerField()
    password=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField(widget=forms.Textarea(attrs={'cols':10,'rows':10}))
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    course=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)