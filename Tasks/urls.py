from django.urls import path
from . import views

urlpatterns = [
    path('', views.TaskListApiView.as_view()),
    path('<int:id>', views.TaskDetailApiView.as_view())
]
