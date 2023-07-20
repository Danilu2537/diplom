from django.urls import path

from core.views import LoginView, ProfileView, SignUpView, UpdatePasswordView

app_name = 'core'

urlpatterns = [
    path('signup', SignUpView.as_view(), name='signup'),  #  /signup
    path('login', LoginView.as_view(), name='login'),  #  /login
    path('profile', ProfileView.as_view(), name='profile'),  #  /profile
    path(
        'update_password', UpdatePasswordView.as_view(), name='update-password'
    ),  #  /update_password
]
