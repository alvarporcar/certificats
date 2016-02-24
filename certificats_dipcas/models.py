from django.db import models
 
class Certificats(models.Model):
   municipi = models.CharField(max_length=100)
   certificat = models.FileField(upload_to=".")
   clau = models.FileField(upload_to=".")
   data_inici = models.DateField(default="2015-01-01")
   data_fi = models.DateField(default="2015-01-01")
   segell = models.BooleanField(default="True")