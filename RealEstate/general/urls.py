from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views as ind_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$',ind_views.home,name='home'),
    url(r'^login/$',ind_views.login_user,{'template_name': 'general/login.html'}, name='login'),
    url(r'^logout/$',ind_views.login_user,{'template_name': 'general/login.html'},name='logout'),
    url(r'^registration/$',ind_views.registration, name='registration')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)