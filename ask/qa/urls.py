from django.urls import re_path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    re_path(r'^$', views.questions_list_all, name='index'),
    re_path('^login/.*$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    re_path(r'^signup/.*$', views.signup, name='signup'),
    re_path(r'^question/(?P<id>[0-9]+)/$', views.get_quest, name='question'),
    re_path(r'^ask/.*$', views.post_add, name='ask'),
    re_path(r'^popular/.*$', views.quests_list_popular, name='popular'),
    re_path(r'^new/.*$', views.test, name='new')
]