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