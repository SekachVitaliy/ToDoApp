from django.urls import path
from .views import index, done_task, delete_task

urlpatterns = [
    path('', index, name='index'),
    path('done/<int:pk>', done_task, name='done_task'),
    path('delete/<int:pk>', delete_task, name='delete_task'),
]
