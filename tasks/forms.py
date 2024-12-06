from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'important']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'White a title'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder':'White a description'}),
            'important': forms.CheckboxInput(attrs={'class': 'form-check-input m-auto'})
        }