from django import forms
from . import models
from django.utils.translation import gettext as _

attrs = {'class': 'form-control'}
class ProjectCreateForm (forms. ModelForm):
    class Meta:
        model = models. Project
        fields = ['title', 'description', 'category']
        labels = {'description' : _('Description'), 'title' : _('Title'), 'category' : _('Category')}
        widgets = {
            'category' : forms. Select (attrs=attrs),
            'description' : forms. Textarea (attrs=attrs),
            'title' : forms. TextInput (attrs=attrs),
        }


class ProjectUpdateForm (forms. ModelForm):
    class Meta:
        model = models. Project
        fields = ['title', 'status', 'category']
        labels = {'title' : _('Title'), 'status' : _('Status'), 'category' : _('Category')}
        widgets = {
            'category' : forms. Select (attrs=attrs),
            'status' : forms. Select (attrs=attrs),
            'title' : forms. TextInput (attrs=attrs),
        }