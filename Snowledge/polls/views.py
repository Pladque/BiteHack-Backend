from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from users.models import UserSkills
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    q = Question.objects.all()
    
    my_skills = UserSkills.objects.filter(user = request.user)

    questions_for_me = []
    questions_not_for_me = []
    found = False
    for question in q:
        for tag in question.tags.all():
            if tag in my_skills:
                questions_for_me.append(question)
                found = True
                break
        if not found:
            questions_not_for_me.append(question)
    return render(request, 'polls/homepage.html', {'questions_for_me': questions_for_me, 'questions_not_for_me':questions_not_for_me})


def add_problem(request):
    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            q = Question()
            q.title = form.cleaned_data['title']
            q.content = form.cleaned_data['question']
            q.solved = False
            q.owner = request.user
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
    return render(request, 'polls/MyQuestions.html', {'questions': my_questions})


def user_skills(request):
    try:
        usr_skills = UserSkills.objects.get(user=request.user)
    except UserSkills.DoesNotExist:
        usr = UserSkills()
        usr.user = request.user
        usr.save()
        usr_skills = UserSkills.objects.get(user=request.user)
    if request.method == 'POST':
        form = AddSkill(request.POST)
        if form.is_valid():
            skill = form.cleaned_data['skill']
            try:
                skill = Tag.objects.get(content=skill)
            except Tag.DoesNotExist:
                s = Tag()
                s.content = skill
                s.save()

            usr_skills.skills.add(skill)
            print(usr_skills.skills.all())
    else:
        form = AddSkill()

    return render(request, 'polls/user_skills.html', {'form': form, 'skills': usr_skills.skills.all()})


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

    this_user_question = False
    if request.user == question.owner:
        this_user_question = True

    return render(request, 'polls/question.html', {'question': question, 'answers': answers, 'this_user_question':this_user_question})

@login_required
def delete_question(request, pk):
    question_id = request.resolver_match.kwargs['pk']
    question = Question.objects.get(id=question_id)

    Question.objects.get(id = question_id).delete()

    q = Question.objects.all()
    return render(request, 'polls/homepage.html', {'questions': q})


@login_required
def mark_as_solved(request, pk):
    question_id = request.resolver_match.kwargs['pk']
    question = Question.objects.get(id=question_id)

    if question.solved == False or question.solved == None:
        question.solved = True
    elif question.solved == True:
        question.solved = False
        
    question.save()

    next = request.POST.get('back', '/')
    return HttpResponseRedirect(next)