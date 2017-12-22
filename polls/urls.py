
"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from polls import views
from django.contrib.auth import views as auth_views
app_name = 'polls'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^index', views.index,name='index'),
    url(r'^about', views.about,name='about'),
    url(r'^contact', views.contact,name='contact'),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^choice', views.choice,name='choice'),
    url(r'^add$', views.add_poll,name='add_poll'),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout,{'next_page': 'out/'}, name='logout'),
    url(r'^logout/out/$', auth_views.login, name='login')
]