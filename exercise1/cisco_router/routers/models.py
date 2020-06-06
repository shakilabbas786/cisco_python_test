from django.db import models

class Routers(models.Model):
    sapid = models.CharField(max_length=50, null=True, blank=True)
    hostname = models.CharField(max_length=50, null=True, blank=True)
    loopback = models.CharField(max_length=50, null=True, blank=True)
    macaddress = models.CharField(max_length=50, null=True, blank=True)
    class Meta:
        db_table = "cisco_routers"
        def __unicode__(self):
            return str(self.sapid)
