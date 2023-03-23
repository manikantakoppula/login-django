from django import forms
from .models import Employee,Department

class AddForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('e_name','e_salary','address','department')
        widgets = {
            'e_name':forms.TextInput(attrs={'class': 'form-control'}),
            'e_salary':forms.NumberInput(attrs={'class': 'form-control'}),
            'address':forms.Textarea(attrs={'class': 'form-control'}),
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['department'].queryset = Department.objects.all()



class AddDepartForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = '__all__'      