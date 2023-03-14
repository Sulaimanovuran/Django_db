from django import forms
from .models import *

class AddNewsForm(forms.Form):
    title = forms.CharField(max_length=255, label='Заголовок:', widget=forms.TextInput(attrs={'class': 'form-input'}))
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    cat = forms.ModelChoiceField(queryset=Category.objects.all(), empty_label='Категория не выбрана')