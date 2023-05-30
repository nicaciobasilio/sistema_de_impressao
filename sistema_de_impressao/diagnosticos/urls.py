from django.urls import path

from . import views

urlpatterns = [
    path('', views.taskList, name='task-list'),
    path('exibir-diagnostico/', views.exibir_diagnostico, name='exibir_diagnostico'),
]