from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from users.models import UserSkills
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    q = Question.objects.all()

    if User.is_authenticated: 
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
    else:
        return render(request, 'polls/homepage.html', {'questions_for_me': [], 'questions_not_for_me':q})


@login_required
def add_problem(request):
    if request.method == 'POST':
        form = NewQuestion(request.POST)
        if form.is_valid():
            request.session['title'] = form.cleaned_data['title']
            request.session['content'] = form.cleaned_data['question']
            request.session['solved'] = False
            request.session['tags'] = form.cleaned_data['tags'].split(' ')
            return HttpResponseRedirect('/similar_results/')
    else:
        form = NewQuestion()
    return render(request, 'polls/add_problem.html', {'form': form})

def get_similar_results(request):
    if request.method == 'POST':
        q = Question()
        q.title = request.session['title']
        q.content = request.session['content']
        q.solved = request.session['solved']
        q.owner = request.user
        q.save()
        q = Question.objects.get(content=request.session['content'])
        for tag in request.session['tags']:
            t = None
            try:
                t = Tag.objects.get(content=tag)
            except Tag.DoesNotExist:
                t = Tag()
                t.content = tag
                t.save()
            q.tags.add(t)
            q.save()
        q.save()
        return HttpResponseRedirect('/my_questions/')
    else:
        questions = get_similar_questions(request.session['content'], request.session['tags'])
        questions = [x[0] for x in questions]
        return render(request, 'polls/similar_results.html', {'questions': questions})

# def get_question(request, question_id):
#     question_object = Question.objects.get(id=question_id)
#     return render(request, 'polls/question.html', {'question_object': question_object})

@login_required
def MyQuestions(request):
    my_questions = Question.objects.filter(owner=request.user)
    return render(request, 'polls/MyQuestions.html', {'questions': my_questions})

@login_required
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
            try:
                usr_skills.skills.add(skill)
            except ValueError:
                request.session['skill'] = skill

    else:
        form = AddSkill()
    return render(request, 'polls/user_skills.html', {'form': form, 'skills': usr_skills.skills.all()})

@login_required
def QuestionDetailView(request, pk):
    question_id = request.resolver_match.kwargs['pk']
    question = Question.objects.get(id=question_id)

    new_answer_content = request.POST.get('answer')        #in html field should be nammed 'answer'
    if new_answer_content is not None:
        ans = Answer()
        ans.content = new_answer_content
        ans.likes = 0
        ans.owner_user = request.user
        ans.owner = question

        ans.save()
    answers = Answer.objects.filter(owner=question)

    this_user_question = False
    if request.user == question.owner:
        this_user_question = True

    tags = question.tags.all()
    return render(request, 'polls/question.html', {'question': question, 'answers': answers, 'this_user_question':this_user_question, 'tags':tags})

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


def get_similar_questions(content, tagss):
    ranking = []
    for quest in Question.objects.all():
        score = 0
        for tag in quest.tags.all():
            for t in tagss:
                if str(tag) == str(t):
                    score += 10
        for word in quest.content.lower().split(' '):
            for w in content.lower().split(' '):
                if str(w) == str(word):
                    score += 1
        ranking.append([quest, score])
    return sorted(ranking, key=lambda x: x[1], reverse=True)
