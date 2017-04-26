from django.conf.urls import url

from .views import OrganismListView, OrganismDetailView, index

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^organisms/$', OrganismListView.as_view(), name='organisms'),
    url(r'^organism/(?P<pk>[0-9]+)/$', OrganismDetailView.as_view(), name='organism'),
]