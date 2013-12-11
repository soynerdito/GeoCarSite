import datetime
import json, urllib2, urllib
import urllib2, base64
import fileinput
from GeoCarImport import GeoCarImport
from time import sleep

url = 'http://127.0.0.1:8000/location/'

def encodeGPS( geoDat ):
	geoDat.parse()
	return urllib.urlencode({
	  "latitude": geoDat.latitude, 
		"longtitude": geoDat.longtitude, 
		"speed": geoDat.speed, 
		"elevation": 0, 
		"timeUTC": geoDat.timeUTC
	})

#request = urllib2.Request(url)
#base64string = base64.encodestring('%s:%s' % ('admin', 'admin')).replace('\n', '')
#request.add_header("Authorization", "Basic %s" % base64string)   

ins = open( 'GPS.txt', 'r' )

success = 0
skip = 0
count=0
for line in ins:
	#skip short lines
	if len(line) < 10:
		continue
	data = GeoCarImport(raw_data= line)
	if data.isValid():
		params = encodeGPS(data)
		try:
			print 'success = ' + str(success)			
			request = urllib2.Request(url)
			base64string = base64.encodestring('%s:%s' % ('admin', 'admin')).replace('\n', '')
			request.add_header("Authorization", "Basic %s" % base64string)   
			result = urllib2.urlopen(request, params)
			#sleep(1)
			success+=1
		except urllib2.HTTPError, e:
			print e.fp.read()			
	else:
		skip+=1
	count+=1
	
ins.close()  

print '*********************************'
print ' Success ' + str(success)
print ' Skipped ' + str(skip)
print ' Total 	' + str(count)

