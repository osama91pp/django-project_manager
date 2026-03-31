from django.contrib.auth.views import LoginView
from django.urls import path, include
from accounts.forms import UserLoginForm
from . import views

urlpatterns = [
    path ('login/', LoginView. as_view (authentication_form= UserLoginForm), name= 'login'),
    path('register/', views.RegestrationView.as_view(template_name='registration/register.html'), name='register'),
    # path ('register/', views. RegestrationView. as_view (), name= 'register'),
    path ('profile/', views. edit_profile, name= 'profile'), # type: ignore
    path ('', include ('django.contrib.auth.urls')),
]