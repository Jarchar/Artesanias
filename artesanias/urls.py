from django.conf.urls import url

from . import views

app_name='artesanias'
urlpatterns = [
    url(r'^$', views.ArtesaniaCrear.as_view(), name='index'),
    url(r'^lista/$', views.ArtesaniaList.as_view, name='artesanias'),
    url(r'^artesanias/(?P<pk>[0-9]+)/$',views.ArtesaniaDetalle.as_view(), name='artesania'),
    url(r'^registro/$', views.ArtesaniaCrear.as_view(), name='registro'),


]
