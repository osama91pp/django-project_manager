from django import forms
from . import models


class ProjectCreateForm (forms. ModelForm):
    class Meta:
        model = models. Project
        fields = ['title', 'description', 'category']
        widgets = {
            'category' : forms. Select (),
            'description' : forms. Textarea (),
            'title' : forms. TextInput (),
        }


class ProjectUpdateForm (forms. ModelForm):
    class Meta:
        model = models. Project
        fields = ['title', 'status', 'category']
        widgets = {
            'category' : forms. Select (),
            'status' : forms. Select (),
            'title' : forms. TextInput (),
        }