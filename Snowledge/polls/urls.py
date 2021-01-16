from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_problem/', add_problem, name='add_problem'),
    path('profile/', user_skills, name='user_skills'),
    path('my_questions/', MyQuestions, name='MyQuestions'),
    path('question/<pk>', QuestionDetailView, name='get_question'),

    path('delete_question/<pk>', delete_question, name='delete_question'),
    path('mark_as_solved/<pk>', mark_as_solved, name='mark_as_solved')
]