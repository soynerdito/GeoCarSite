import datetime
import json, urllib2, urllib
import urllib2, base64


url = 'http://127.0.0.1:8000/location/'

params = urllib.urlencode({
  "latitude": "44.3", 
    "longtitude": "33.4", 
    "speed": "12", 
    "elevation": "12", 
    "timeUTC": "1998-01-11T01:00:00"
})

request = urllib2.Request(url)
base64string = base64.encodestring('%s:%s' % ('admin', 'admin')).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string)   

try:
    result = urllib2.urlopen(request, params)    
except urllib2.HTTPError, e:
    print e.fp.read()



