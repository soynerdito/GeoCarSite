from django.forms.models import modelformset_factory
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from django.template import Context, loader
from django.views import generic
from location.models import Location
import os
import os.path

def index(request):
    #entries = Item.objects.all()     
    #t = loader.get_template(os.path.join(os.path.dirname(__file__),'templates/index.html'))
    #return HttpResponse(t.render())
    #return render_to_response(os.path.join(os.path.dirname(__file__),'templates/leaflet_sample.html'), locals())    
    locations = Location.objects.all()    
    t = loader.get_template(os.path.join(os.path.dirname(__file__),'templates/index2.html'))    
    c = Context({
        'location_list': locations,
    })
    print 'LOCATIONS ***************'
    return HttpResponse(t.render(c))
    #return render_to_response(os.path.join(os.path.dirname(__file__),'templates/index2.html'), locals())


def home(request):
    t = loader.get_template(os.path.join(os.path.dirname(__file__),'templates/startpage.html'))        
    return HttpResponse(t.render( Context() ))

def video_player(request, token, raw_data=None ):
    print 'Video Player'
    print token
    
    print raw_data
    locations = Location.objects.all()    
    t = loader.get_template(os.path.join(os.path.dirname(__file__),'templates/index2.html'))    
    c = Context({
        'location_list': locations,
    })
    print 'LOCATIONS ***************'
    return HttpResponse(t.render(c))
