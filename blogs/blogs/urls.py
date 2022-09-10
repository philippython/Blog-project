from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('post/<int:post_id>', views.post_text, name='post'),
    path('new_post/', views.new_post, name='new_post'),

    path('edit_post_text/<int:post_id>',
        views.edit_post_text, name='edit_post_text'),
]
