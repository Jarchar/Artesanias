from django.conf.urls import include, url

from . import views

app_name='artesanias'
urlpatterns = [
    url(r'^$', views.ArtesaniaCrear.as_view(), name='index'),
    url(r'^artesanias/$', views.ArtesaniaList.as_view, name='artesanias'),
    url(r'^artesanias/(?P<pk>[0-9]+)/$',views.ArtesaniaDetalle.as_view(), name='artesania'),
    url(r'^artesanias/registrar/$', views.ArtesaniaCrear.as_view(), name='registro'),
    url(r'^clientes/', include('registration.backends.hmac.urls')),


]
