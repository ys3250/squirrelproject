from django import forms

class AddForm(forms.Form):
    unique_squirrel_id = forms.CharField(label='ID', max_length=100)
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField()
    cc_myself = forms.BooleanField(required=False)
