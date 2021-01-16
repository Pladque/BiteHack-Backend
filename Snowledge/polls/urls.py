from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_problem/', add_problem, name='add_problem'),
    path('question/<question_id>', get_question, name='get_question')
]