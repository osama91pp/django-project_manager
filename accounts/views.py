from django.shortcuts import redirect, render
from django.views.generic import CreateView
from .forms import UserRegistrationForm, ProfileForm
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.

class RegestrationView(CreateView):
    form_class = UserRegistrationForm
    template_name = 'registration/regester.html'
    # success_url = reverse_lazy('login')

    def get_success_url(self):
        login (self.request, self.object) # type: ignore
        return reverse_lazy ('project_list')

@login_required # type: ignore
def edit_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')

    else:
        form = ProfileForm(instance=request.user)
        return render(
            request,
            'profile.html',
            {'form': form}
            )
