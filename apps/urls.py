from django.urls import path
from .views import home, delete_task, toggle_task, edit_task,logout_view,  register


urlpatterns = [
    path('', home, name='home'),

    path('toggle/<int:id>/', toggle_task, name='toggle_task'),
    path('edit/<int:id>/', edit_task, name='edit_task'),
    path('delete/<int:id>/', delete_task, name='delete_task'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]