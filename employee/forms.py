from django import forms
from django.forms.models import inlineformset_factory
from.models import Employee, Qualification


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = '__all__'


class QualificationForm(forms.ModelForm):

    class Meta:
        model = Qualification
        exclude = ['employee']

QualificationFormSet = inlineformset_factory(Employee, Qualification, form=QualificationForm, extra=1)
