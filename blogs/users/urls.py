from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('', include('django.contrib.auth.urls')),
    
    #Registration page
    path('register/', views.register, name='register'),
]

# TODO: in the homepage if user is not logged in erase all entries
