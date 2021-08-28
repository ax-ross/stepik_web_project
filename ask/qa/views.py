from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def quests_list_all(request):
    quests = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(quests, 10)
    paginator.baseurl = '/?page='
    page = paginator.get_page(page)
    return render(request, 'quests_list.html', {
        'quests': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def quests_list_popular(request):
    quests = Question.objects.popular()
    page = request.GET.get('page', 1)
    paginator = Paginator(quests, 10)
    paginator.baseurl = '/?page='
    page = paginator.page(page)
    return render(request, 'quests_list.html', {
        'quests': page.object_list,
        'paginator': paginator,
        'page': page,
    })


def get_quest(request, id):
    quest = get_object_or_404(Question, pk=id)
    return render(request, 'quests.html', {
        'quest': quest
    })
