from django.shortcuts import render
from django.views.generic import ListView,  CreateView, UpdateView, DeleteView
from django. urls import reverse_lazy, reverse
from . import models
from . import forms
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
class ProjectListView (LoginRequiredMixin, ListView):
    model = models. Project
    template_name = 'project/list.html'
    paginate_by = 6

    def get_queryset(self):
        query_set = super().get_queryset()
        where = {}
        q = self. request. GET. get ('q', None)
        if q:
            where ['title__icontains'] = q
        return query_set. filter (**where)



class ProjectCreateView (LoginRequiredMixin, CreateView):
    model = models. Project
    form_class = forms. ProjectCreateForm
    template_name = 'project/create.html'
    success_url = reverse_lazy ('project_list')


class ProjectUpdateView (LoginRequiredMixin, UpdateView):
    model = models. Project
    form_class = forms. ProjectUpdateForm
    template_name = 'project/update.html'

    def get_success_url(self):
        return reverse ('project_update', args=[self. object. id]) # type: ignore

class ProjectDeleteView (LoginRequiredMixin, DeleteView):
    model = models. Project
    template_name = 'project/delete.html'
    success_url = reverse_lazy ('project_list')


from django.shortcuts import render, redirect
from django.contrib import messages

class TaskCreateView (LoginRequiredMixin, CreateView):
    model = models. Task
    fields = ['description', 'project']
    http_method_names = ['post']

    def post(self, request, *args, **kwargs):
        # refuse empty descriptions to avoid invalid form/template errors
        description = request.POST.get('description', '').strip()
        project_id = request.POST.get('project')
        if not description:
            # warn the user instead of crashing
            if project_id:
                messages.warning(request, "Task description cannot be empty.")
            return redirect(reverse('project_update', args=[project_id]))
        return super().post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse ('project_update', args=[self. object. project. id]) # type: ignore


class TaskUpdateView (LoginRequiredMixin, UpdateView):
    model = models. Task
    fields = ['is_completed']
    http_method_names = ['post']

    def get_success_url(self):
        return reverse ('project_update', args=[self. object. project. id]) # type: ignore


class TaskDeleteView (LoginRequiredMixin, DeleteView):
    model = models. Task

    def get_success_url(self):
        return reverse ('project_update', args=[self. object. project. id]) # type: ignore