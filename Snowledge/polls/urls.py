from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('add_problem/', add_problem, name='add_problem')
]