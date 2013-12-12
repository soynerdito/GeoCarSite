
#$GPRMC,225446,A,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68
#225446       Time of fix 22:54:46 UTC
#A            Navigation receiver warning A = OK, V = warning
#4916.45,N    Latitude 49 deg. 16.45 min North
#12311.12,W   Longitude 123 deg. 11.12 min West
#000.5        Speed over ground, Knots
#054.7        Course Made Good, True
#191194       Date of fix  19 November 1994
#020.3,E      Magnetic variation 20.3 deg East
#*68          mandatory checksum


class GeoCarImport(object):
	GPRMC_TIME			= 1
	GPRMC_WARNING		= 2
	GPRMC_LAT			= 3
	GPRMC_LAT_CARD		= 4
	GPRMC_LONG			= 5
	GPRMC_LONG_CARD		= 6
	GPRMC_SPEED			= 7
	GPRMC_GOOD_C		= 8
	GPRMC_DATE			= 9
	GPRMC_MAGNETIC		= 10
	GPRMC_MAGNETIC_CARD	= 11

	latitude = 0
	longtitude = 0
	speed = 0
	elevation = 0
	timeUTC = 0
	
	def isValid(self):
		return True if self.data_split[GeoCarImport.GPRMC_WARNING]=='A' else False

	def cast_raw_date(self):
		#sample of raw data
		#$GPRMC,233515.000,A,,N,,W,0.02,357.57,091213,,,D*7:1413,1121,1299
		#"timeUTC": "1998-01-11T01:00:00"		
		#date and time are separate		
		date = self.data_split[self.GPRMC_DATE]
		time = self.data_split[self.GPRMC_TIME]		
		#{"timeUTC": ["Datetime has wrong format. Use one of these formats instead: YYYY-
#MM-DDThh:mm[:ss[.uuuuuu]][+HHMM|-HHMM|Z]"]}
		return '20{0}-{1}-{2}T{3}:{4}:{5}'.format(date[4:6],date[2:4],date[0:2],
			time[0:2],time[2:4],time[4] )
			#time[0:2],time[2:4],time[4:6], str(int(float(time[6:])*100)) )
		
	def cast_raw_coord(self, coord, cardinal ):
		coord_fix = 0
		if len(coord.strip())>0 and len(cardinal) > 0:
			pos = coord.find('.')
			integer_part = coord[:(pos-2)]	
			decimal_part = float(coord[(pos-2):])/60
			coord_fix = float(integer_part) + decimal_part
			if cardinal.upper() == 'S' or cardinal.upper() == 'W':
				coord_fix = coord_fix  * -1
		return coord_fix
	
	def __init__(self, raw_data=None ):
		self.raw_data = raw_data
		#split in fields
		self.data_split = self.raw_data.split(',')
	
	def parse(self):
		#do the parsing
		
		raw_lat = self.data_split[self.GPRMC_LAT]
		self.lat_cardinal = self.data_split[GeoCarImport.GPRMC_LAT_CARD]
		
		raw_long = self.data_split[self.GPRMC_LONG]
		self.long_cardinal = self.data_split[GeoCarImport.GPRMC_LONG_CARD]
		
		self.latitude = str(self.cast_raw_coord( raw_lat, self.lat_cardinal ))
		self.longtitude =  str(self.cast_raw_coord( raw_long, self.long_cardinal ))
		self.timeUTC = self.cast_raw_date()		

	def verbose(self):
		print 'Lat='  + str(self.latitude)
		print 'Long='  + str(self.longtitude)
		print 'Speed=' + str(self.speed)
		print 'Elev='  + str(self.elevation)
		print 'Time='  + str(self.timeUTC)
