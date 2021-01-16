from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *

# Create your views here.
def index(request):
    q = Question.objects.all()
    return render(request, 'polls/homepage.html', {'questions': q})


def add_problem(request):
    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            q = Question()
            q.title = form.cleaned_data['title']
            q.content = form.cleaned_data['question']
            q.save()
            for tag in form.cleaned_data['tags'].split(','):
                t = None
                try:
                    t = Tag.objects.get(content=tag)
                except Tag.DoesNotExist:
                    t = Tag()
                    t.content = tag
                    t = t.save()
                q.tags.add(t)
            q.save()
    else:
        form = NewQuestion()
    return render(request, 'polls/add_problem.html', {'form': form})


# def get_question(request, question_id):
#     question_object = Question.objects.get(id=question_id)
#     return render(request, 'polls/question.html', {'question_object': question_object})


@login_required
def MyQuestions(request):
    my_questions = Question.objects.filter(owner=request.user)
    return render(request, 'polls/MyQuestions.html', {'my_questions': my_questions})

def QuestionDetailView(request, pk):
    question_id = request.resolver_match.kwargs['pk']
    question = Question.objects.get(id=question_id)

    new_answer_content = request.POST.get('answer')        #in html field should be nammed 'answer'
    
    if new_answer_content is not None:
        ans = Answer()
        ans.content = new_answer_content
        ans.likes = 0
        ans.owner = question

        ans.save()

    answers = Answer.objects.filter(owner=question)

    return render(request, 'polls/question.html', {'question': question, 'answers': answers})