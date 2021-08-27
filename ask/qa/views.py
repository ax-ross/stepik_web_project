from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from .models import Question

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def quest_list_all(request):
    quests = Question.objects.new()
    page = request.GET.get('page', 1)
    paginator = Paginator(quests, 10)
    paginator.baseurl =  '/?page=2'
    page = paginarot.page(page)
    return render(request, 'templates/quests_list.html', {
        'quests': page.object_list,
        'paginator': paginator,
        'page': page,
        })
