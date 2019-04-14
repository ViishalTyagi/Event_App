from django.urls import path
from .views import SignUpView, LoginView, setPreferences, getEvents


app_name = 'users'

urlpatterns = [
    path('users/', SignUpView.as_view(), name="register"),
    path('users/login/', LoginView.as_view(), name="login"),
    path('users/setPreferences/', setPreferences.as_view(), name="pref"),
    path('users/getEvents/', getEvents.as_view(), name='Events'),
]