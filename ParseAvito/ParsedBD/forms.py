from .models import UserRequest
from django.forms import ModelForm, TextInput


class UserRequestForm(ModelForm):
    class Meta:
        model = UserRequest
        fields = ['region', 'request_words']

        widgets = {
            "region": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Регион',
            }),
            "request_words": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ключевое слово',
            }),
        }
