from django.urls import path
from . import views

urlpatterns = [
    path('', views.question_form, name='form'),
    path('answers/', views.view_answers, name='answers'),
]