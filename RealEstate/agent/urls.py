from django.conf.urls import include, url
from django.contrib import admin
from . import views as ind_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
   url(r'^$',ind_views.home,name='home'),
   url(r'^requests/$',ind_views.buyerrequests,name='buyerrequests'),
   url(r'^chat/$',ind_views.chat,name='chat'),
   url(r'^chat/with/(?P<uid>\d+)/$',ind_views.chatbegin,name='chatbegin'),
   url(r'^property/details/(?P<pk>\d+)/$',ind_views.aboutprop,name='aboutprop'),
   url(r'^make/request/(?P<pid>\d+)/(?P<uid>\d+)/$',ind_views.makerequest,name='makerequest'),
   url(r'^updatests/(?P<pid>\d+)/$',ind_views.updatereq,name='updreq'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)