from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import RegisterView
from .forms import LoginForm

from . import views

app_name = "users"

urlpatterns = [
    path(
        "login",
        LoginView.as_view(
            template_name="users/login.html",
            authentication_form=LoginForm,
            redirect_authenticated_user=True,
        ),
        name="login",
    ),
    path("logout", LogoutView.as_view(), name="logout"),
    path("signup", RegisterView.as_view(), name="signup"),
    path('profile/', views.profile, name='profile'),
]
