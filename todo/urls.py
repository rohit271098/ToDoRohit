from django.urls import path
from .views import TaskList, TaskDetail

urlpatterns = [
    path('', TaskList.as_view(), name="task"),  # it automatically imports task_list.html file
    path('task/<int:pk>/', TaskDetail.as_view(), name="tasks-detail"),
]
