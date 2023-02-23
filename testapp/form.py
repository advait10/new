from django import forms
from testapp.models import Employee

class Employee_Reg(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
