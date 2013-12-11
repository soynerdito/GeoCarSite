#$GPRMC,235944.800,V,,,,,0.00,0.00,050180,,,N*4:1530,1215,1385

raw_data = '$GPRMC,225446,A,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68'
#eg2. $GPRMC,225446,A,4916.45,N,12311.12,W,000.5,054.7,191194,020.3,E*68
#225446       Time of fix 22:54:46 UTC
#A            Navigation receiver warning A = OK, V = warning
#4916.45,N    Latitude 49 deg. 16.45 min North
#12311.12,W   Longitude 123 deg. 11.12 min West
#000.5        Speed over ground, Knots
#054.7        Course Made Good, True
#191194       Date of fix  19 November 1994
#020.3,E      Magnetic variation 20.3 deg East
#*68          mandatory checksum

#Field locations
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

data_split = raw_data.split(',')
print data_split



raw_lat = data_split[GPRMC_LAT]
lat_cardinal = data_split[GPRMC_LAT_CARD]
raw_long = data_split[GPRMC_LONG]
long_cardinal = data_split[GPRMC_LONG_CARD]


print 'Org Lat' + raw_lat
print cast_raw_coord( raw_lat, lat_cardinal )

print 'Org Long' + raw_long
print cast_raw_coord( raw_long, long_cardinal )

