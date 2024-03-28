from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views as ind_views

urlpatterns = [
    url(r'^$',ind_views.home,name='home'),
    url(r'^upload/house-details/$',ind_views.uploadPropertyDetails,name='uploadproperty'),
    url(r'^location/spot/$',ind_views.locationspot,name='locationdetails'),
    url(r'^location/spot/found/(?:(?P<lati>.+))?/(?:(?P<loni>.+))?/(?:(?P<address>.+))?/$',ind_views.locationspotfound,name='locationfound'),
    url(r'^location/nearest/$',ind_views.nearestlocation,name='nearestlocations'),
    url(r'^property-details/(?P<pk>\d+)/$',ind_views.aboutprop,name='aboutprop'),
    url(r'^property-location-details/(?P<pk>\d+)/$',ind_views.aboutproploc,name='aboutproploc'),
    url(r'^chat/$',ind_views.chat,name='chat'),
    url(r'^chat/with/(?P<uid>\d+)/$',ind_views.chatbegin,name='chatbegin'),
	url(r'^chart/$',ind_views.chart,name='chart'),
    url(r'^line/$',ind_views.line,name='line'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
