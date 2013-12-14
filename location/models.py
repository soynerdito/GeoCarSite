from django.db import models

class Vehicle( models.Model ):
    name = models.CharField(max_length=200)
    description = models.TextField()
    serial = models.CharField(max_length=200)    
    
    def __unicode__( self ):
        return '%s' % ( self.description )
    
    class Meta:
        verbose_name = "Vehicle"
        verbose_name_plural = "Vehicles"


class Location( models.Model ):
    latitude = models.DecimalField(max_digits=15, decimal_places=10)
    longtitude = models.DecimalField(max_digits=15, decimal_places=10)
    speed = models.DecimalField(max_digits=10, decimal_places=4)
    elevation = models.DecimalField( max_digits=15, decimal_places=4 )    
    timeUTC = models.DateTimeField()
    recTimestamp = models.DateTimeField(auto_now_add=True)
    #source = models.ForeignKey(Vehicle)
    def __unicode__( self ):
        return '%s' % ( self.latitude )
    
    class Meta:
        verbose_name = "Location"
        verbose_name_plural = "Locations"


class PSoCMessage( models.Model ):
    token = models.CharField(max_length=50)
    raw_data = models.CharField(max_length=200)
    
    def __unicode__( self ):
        return '%s' % ( self.raw_data )

    class Meta:
        verbose_name = "PSoCMessage"
        verbose_name_plural = "PSoCMessages"

