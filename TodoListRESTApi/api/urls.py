from django.urls import path
from . import views
urlpatterns = [
    path('', view=views.apiOverview, name='apiOverview'),
    path('tasklist', view=views.taskList, name='tasklist'),

]
