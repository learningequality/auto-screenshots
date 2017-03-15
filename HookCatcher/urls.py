from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^state/$', views.allStates, name='allStates'),
    url(r'^state/branch/(?P<branchName>[a-zA-Z1-9:;_-]+)/$',
        views.singleBranch, name='singleBranch'),
    url(r'^state/pr/(?P<prNumber>[1-9]+)/$', views.singlePR, name='singlePR'),
    url(r'^img/(?P<imageID>[a-zA-Z1-9_.-]+)/$',
        views.getImage, name='getImage'),
]
