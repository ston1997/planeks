from django import forms
from .models import Column, Schema, DataSet

from extra_views import InlineFormSetFactory


class SchemaForm(forms.ModelForm):

    class Meta:
        model = Schema
        fields = '__all__'

        widgets = {
            "owner": forms.HiddenInput(),
            "name": forms.TextInput(),
            "delimiter": forms.Select(),
            "quote_character": forms.Select(),
        }


class ColumnForm(forms.ModelForm):

    class Meta:
        model = Column
        fields = '__all__'

        widgets = {
            "name": forms.TextInput(),
            "order": forms.NumberInput(),
            "data_type": forms.Select(),
            "data_range_from": forms.NumberInput(),
            "data_range_to": forms.NumberInput(),
        }


class DataSetForm(forms.ModelForm):

    class Meta:
        model = DataSet
        fields = '__all__'


class SchemaColumnInline(InlineFormSetFactory):
    model = Column
    form_class = ColumnForm
    fields = "__all__"

    factory_kwargs = {
        "extra": 1,
        "max_num": None,
        "can_order": False,
        "can_delete": True,
    }
