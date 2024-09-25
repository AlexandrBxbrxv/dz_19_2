from django import forms
from django.forms import BooleanField

from catalog.models import Consumable, Version

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ConsumableForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Consumable
        exclude = ('created_at', 'updated_at', 'purchases_count', 'creator')

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


class ConsumableModeratorForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Consumable
        fields = ('description', 'category', 'is_published')

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


class VersionForm(StyleFormMixin, forms.ModelForm):
    class Meta:
        model = Version
        fields = "__all__"
