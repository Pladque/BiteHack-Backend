from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'polls/index.html')

def add_problem(request):
    return 1

@login_required
def MyQuestions(request):
    my_questions = Question.objects.filter(owner=request.user)
    return render(request, 'polls/MyQuestions.html',{'my_questions' : my_questions })