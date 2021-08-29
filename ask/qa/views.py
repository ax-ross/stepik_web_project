from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Question


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def paginate_question(request, qs):
    limit = 10
    page = request.GET.get('page', 1)
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return page


def quests_list_all(request):
    quests_list = Question.objects.new()
    quests = paginate_question(request, quests_list)
    return render(request, 'quests_list.html', {
        'quests': quests,
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
