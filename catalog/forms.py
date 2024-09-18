from django import forms
from django.forms import BooleanField

from catalog.models import Consumable

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ConsumableForm(forms.ModelForm):
    class Meta:
        model = Consumable
        exclude = ('created_at', 'updated_at', 'purchases_count',)

    def clean_name(self):
        clean_name = self.cleaned_data['name']
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in clean_name:
                raise forms.ValidationError('Наименование не должно содержать запрещенных слов')
        return clean_name

    def clean_description(self):
        clean_description = self.cleaned_data['description']
        for forbidden_word in FORBIDDEN_WORDS:
            if forbidden_word in clean_description:
                raise forms.ValidationError('Описание не должно содержать запрещенных слов')
        return clean_description

