from django.urls import path
from . import views

app_name = 'userprofile'

urlpatterns = [
    # Other URL patterns...
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
]