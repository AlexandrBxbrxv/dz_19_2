from django import forms

from catalog.models import Consumable

FORBIDDEN_WORDS = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']


class ConsumableForm(forms.ModelForm):
    class Meta:
        model = Consumable
        exclude = ('created_at', 'updated_at', 'purchases_count',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'

    def clean_name(self):
        clean_data = self.cleaned_data()['name']
        if FORBIDDEN_WORDS in clean_data:
            raise forms.ValidationError('Наименование не должно содержать запрещенных слов')
        return

    def clean_description(self):
        clean_data = self.cleaned_data()['description']
        if FORBIDDEN_WORDS in clean_data:
            raise forms.ValidationError('Описание не должно содержать запрещенных слов')
        return

