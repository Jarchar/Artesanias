from django.conf.urls import url

from . import views

app_name='artesanias'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^$', views.ArtesaniaList.as_view, name='artesanias'),
    url(r'^artesanias/(?P<pk>[0-9]+)/$',views.ArtesaniaView.as_view(), name='artesania'),


]
