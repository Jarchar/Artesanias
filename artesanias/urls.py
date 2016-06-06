from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
app_name='artesanias'
urlpatterns = [
    url(r'^$', views.ArtesaniaCrear.as_view(), name='index'),
    url(r'^galeria/$', views.ArtesaniaList.as_view(), name='artesanias-lista'),
    url(r'^artesanias/(?P<pk>[0-9]+)/$',views.ArtesaniaDetalle.as_view(), name='artesania-detalle'),
    url(r'^artesanias/registrar/$', views.ArtesaniaCrear.as_view(), name='artesania-add'),
    url(r'^clientes/', include('registration.backends.hmac.urls')),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

