from django.conf.urls.defaults import patterns, include, url
from django.views.generic import DetailView, ListView, TemplateView
from rick.models import RickrollStory

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name="rick/home.html"), name='home'),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model=RickrollStory), name='home'),
)
