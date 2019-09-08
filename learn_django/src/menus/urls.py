from django.conf.urls import url

from .views import (
        ItemDetailView,
        ItemListView,
        ItemCreateView,
        ItemUpdateView,
)
#from restaurants.views import HomeView, AboutView, ContactView
urlpatterns = [
    url(r'^create/$', ItemCreateView.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/edit/$', ItemUpdateView.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/$', ItemDetailView.as_view(), name='detail'),
    url(r'^$', ItemListView.as_view(), name='list'),
]
