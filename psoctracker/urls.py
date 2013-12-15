from django.conf.urls import patterns, include, url
#from django.conf.urls.defaults import url, patterns, include
from django.contrib.auth.models import User, Group
from rest_framework import viewsets, routers
from location.models import Location, PSoCMessage
from django.views.generic import TemplateView

# ViewSets define the view behavior.
class LocationViewSet(viewsets.ModelViewSet):
    model = Location

class PSoCMessageViewSet(viewsets.ModelViewSet):
	model = PSoCMessage

# Routers provide an easy way of automatically determining the URL conf
router = routers.DefaultRouter()
router.register(r'location', LocationViewSet)
router.register(r'psocmessage', PSoCMessageViewSet)


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',    
	url(r'^admin', include(admin.site.urls)),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^test', 'location.views.index', name="home2"),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^partner/(?P<token>[-\w]+)/(?P<raw_data>\w+)/$', 'location.views.video_player'),
    url(r'^', 'location.views.home', name="home"),
#PSoCMessage
    #url(r'^contact$', TemplateView.as_view(template_name='contact.html'), name="contact"),
    #url(r'^form$', 'demo_app.views.demo_form'),
    #url(r'^form_template$', 'location.views.demo_form_with_template'),
    #url(r'^form_inline$', 'location.views.demo_form_inline'),
    #url(r'^formset$', 'location.views.demo_formset', {}, "formset"),
    #url(r'^tabs$', 'demo_app.views.demo_tabs', {}, "tabs"),
    #url(r'^pagination$', 'location.views.demo_pagination', {}, "pagination"),
    #url(r'^widgets$', 'demo_app.views.demo_widgets', {}, "widgets"),
    #url(r'^buttons$', TemplateView.as_view(template_name='buttons.html'), name="buttons"),
    
    # Uncomment the next line to enable the admin:
    
)
