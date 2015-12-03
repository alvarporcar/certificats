from django.db import models
 
class Certificats(models.Model):
   municipi = models.CharField(max_length=100)
   certificat = models.FileField(upload_to=".")
   clau = models.FileField(upload_to=".")