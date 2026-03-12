from django import forms
from . import models

attrs = {'class': 'form-control'}
class ProjectCreateForm (forms. ModelForm):
    class Meta:
        model = models. Project
        fields = ['title', 'description', 'category']
        widgets = {
            'category' : forms. Select (attrs=attrs),
            'description' : forms. Textarea (attrs=attrs),
            'title' : forms. TextInput (attrs=attrs),
        }


class ProjectUpdateForm (forms. ModelForm):
    class Meta:
        model = models. Project
        fields = ['title', 'status', 'category']
        widgets = {
            'category' : forms. Select (attrs=attrs),
            'status' : forms. Select (attrs=attrs),
            'title' : forms. TextInput (attrs=attrs),
        }