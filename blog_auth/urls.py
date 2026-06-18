from django.urls import path
from .views import RegisterView, LoginView, LogoutView, ProfileView

urlpatterns  = [
    path('signup/', RegisterView.as_view()),
    path('Login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('Profile/', ProfileView.as_view()),

]