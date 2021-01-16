from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_problem/', add_problem, name='add_problem'),
    path('profile/', user_skills, name='user_skills'),
    path('my_questions/', MyQuestions, name='MyQuestions'),
    path('skills/', user_skills, name='user_skills'),
    path('question/<pk>', QuestionDetailView, name='get_question'),

    path('question/<pk>', delete_question, name='delete_question'),
    path('question/<pk>', mark_as_solved, name='mark_as_solved')
]