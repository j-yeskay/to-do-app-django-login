from django import forms
from . models import ToDoItem

class CreateToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['task','author']

        widgets = {
                'tasks' : forms.TextInput(attrs = {'class' : 'form-control'}),
                'author' : forms.TextInput(attrs = {'value' : '' , 'id':'sk' , 'type' : 'hidden'}),
                #'author' : forms.Select(attrs = {'class' : 'form-control'}),
        }

class EditToDoForm(forms.ModelForm):
    class Meta:
        model = ToDoItem
        fields = ['task']
        widgets = {
                'tasks' : forms.TextInput(attrs = {'class' : 'form-control'}),
        }
