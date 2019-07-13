from django import forms
from model_app.models import ContactModel

class BasicForm(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ConsoleFile(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    message = forms.CharField(widget=forms.Textarea)

class ContactForm(forms.ModelForm):
    class Meta():
        model = ContactModel
        fields = ('name', 'email', 'message')
        # fileds = '__all__'
        widgets = {
                'name' : forms.TextInput(attrs={'class':'form-style'}),
                'email' : forms.EmailInput(attrs={'class':'form-style'}),
                'message' : forms.Textarea(attrs={'class':'form-style'})
        }

class MoreForm(forms.Form):
    GENDER_FIELD = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    EDU_FIELD = [
        ('niit', 'NIIT'),
        ('hiit', 'HIIT'),
        ('alabian', 'Alabian'),
    ]

    REF_FIELD = [
        ('facebook', 'Facebook'),
        ('nairaland', 'Nairaland'),
        ('twitter', 'Twitter'),
    ]
    name = forms.CharField(label='Your name', widget=forms.TextInput(attrs={'class':'form-style', 'placeholder':'Enter name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-style'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-style'}))
    gender = forms.CharField(widget=forms.RadioSelect(choices=GENDER_FIELD))
    education = forms.CharField(widget=forms.CheckboxSelectMultiple(choices=EDU_FIELD))
    referer = forms.CharField(widget=forms.Select(attrs={'class':'form-style'}, choices=REF_FIELD))
    message = forms.CharField(widget=forms.Textarea(attrs={'class':'form-style'}))
