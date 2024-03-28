"""RealEstate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from general.urls import urlpatterns as general_urls
from buyer.urls import urlpatterns as buyer_urls
from seller.urls import urlpatterns as seller_urls
from agent.urls import urlpatterns as agent_urls
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(general_urls, namespace='generals'),name='generals'),
    url(r'^buyer/',include(buyer_urls, namespace='buyers'),name='buyers'),
    url(r'^seller/',include(seller_urls, namespace='sellers'),name='sellers'),
    url(r'^agent/',include(agent_urls, namespace='agents'),name='agents'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
