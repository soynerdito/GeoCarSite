from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from location.models import Location

# ViewSets define the view behavior.
class LocationViewSet(viewsets.ModelViewSet):
    model = Location

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^test', 'location.views.index'),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    # Examples:
    # url(r'^$', 'psoctracker.views.home', name='home'),
    # url(r'^psoctracker/', include('psoctracker.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
