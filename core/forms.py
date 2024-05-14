from django import forms
from django.contrib.auth.forms import (
    UserCreationForm,
)
from core.models import (
    User,
)

class SignUpForm(UserCreationForm):
    is_active = forms.BooleanField(widget=forms.HiddenInput(), initial=True)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        del self.fields['password2']
        self.fields['is_active'].required = False
        self.fields['is_active'].initial = True
        self.fields['is_active'].widget.attrs.update({'value': True})
        self.fields['name'].widget.attrs.update({'required': '', 'name': 'name', 'id': 'inputname', 'type': 'text', 'placeholder': 'Enter Name'})
        self.fields['email'].widget.attrs.update({'required': '', 'name': 'email', 'id': 'inputemail', 'type': 'email', 'placeholder': 'example@email.com'})
        self.fields['phone'].widget.attrs.update({'required': '', 'name': 'phone', 'id': 'inputphone', 'type': 'text', 'placeholder': '9876543210'})
        self.fields['address'].widget.attrs.update({'required': '', 'name': 'pan', 'id': 'inputpan', 'type': 'text', 'placeholder': '121 St'})

    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'address', 'password1', 'is_active']
        exclude = ['password2']

class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'
        self.fields['title'].widget.attrs.update({'required': '', 'name': 'blogtitle', 'id': 'blogtitle', 'type': 'text'})
        self.fields['status'].widget.attrs.update({'required': '', 'name': 'blogtitle', 'id': 'blogtitle', 'type': 'text'})
