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
from django.contrib import admin
from . import views
from django.views.generic import TemplateView
from django.contrib.auth.views import login
app_name='polls'
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.Indexview.as_view(), name='index'),
    # url(r'^hello$', views.hello, name='hello'),
    # url(r'^([0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.Detailview.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<pk>[0-9]+)/results/$', views.Resultview.as_view(), name='results'),
    # url(r'^connection/',TemplateView.as_view(template_name = 'polls/login.html')),
    url(r'^login/', views.login, name = 'login'),
    url(r'^success/', views.success, name = 'success'),
    url(r'^logout/', views.logout, name = 'logout'),
    url(r'^home/', views.home, name='home')
]
