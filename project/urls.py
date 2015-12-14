"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""

from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^detail_view/(?P<pk>\d+)/$', 'main.views.detail_view'),
    url(r'^list_view/$', 'main.views.list_view'),

    url(r'^cereal_types/$', 'main.views.cereal_types'),
    url(r'^cereal_details/(?P<pk>\d+)/$', 'main.views.cereal_details'),
    url(r'^brand/$', 'main.views.brands'),
    url(r'^brand_details/(?P<pk>\d+)/$', 'main.views.brand_details'),
    url(r'^main_page/$', 'main.views.main_page'),

    
    url(r'^create_view/$','main.views.create_view'),
    url(r'^create_view2/$','main.views.create_view2'),

    url(r'^json_response/$', 'main.views.json_response'),
    url(r'^ajax_template/$', 'main.views.ajax_search'),

    #url(r'^update_view/(?P<pk>\d+)/$', 'main.view.update_view'),
    #url(r'^delete_view/(?P<pk>\d+)/$', 'main.view.delete_view'),

    #url(r'^signup/$', 'main.view.signup'),
    #url(r'^login_view/$', 'main.view.login_view'),
    #url(r'^logout_view/$', 'main.views.logout_view'),

    #url(r'^', include('project.urls')),
    #url(r'^cereals/$', views.cereal_list),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns = format_suffix_patterns(urlpatterns)
