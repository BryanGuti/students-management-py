from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'student_number',
            'first_name',
            'last_name',
            'email',
            'career',
            'gpa',
        ]
        labels = {
            'student_number': 'Student code',
            'first_name': 'First name',
            'last_name': 'Last name',
            'email': 'Email',
            'career': 'Carrer',
            'gpa': 'Gpa',
        }
        widgets = {
            'student_number': forms.NumberInput(attrs={
                'class': 'form-control'
            }),
            'first_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'last_name': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control'
            }),
            'career': forms.TextInput(attrs={
                'class': 'form-control'
            }),
            'gpa': forms.NumberInput(attrs={
                'class': 'form-control'
            })
        }
