from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator, EmptyPage
from .models import Question
from .forms import AskForm, AnswerForm


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate(request, qs):
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    paginator.baseurl = '/?page='
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def questions_list_all(request):
    questions_list = Question.objects.new().order_by('-id')
    questions = paginate(request, questions_list)
    return render(request, 'questions_list.html', {
        'questions': questions,
    })


def quests_list_popular(request):
    questions = Question.objects.popular()
    questions = paginate(request, questions)
    return render(request, 'popular_questions.html', {
        'questions': questions,
    })


def get_quest(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save()
            url = answer.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': id})
    question = get_object_or_404(Question, pk=id)
    answers = question.answer_set.all()
    return render(request, 'questions.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })


def post_add(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'question_add.html', {
        'form': form
    })

