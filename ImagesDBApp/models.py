from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#models.py

class Imagen(models.Model):
	nombreImg = models.CharField(blank=True, null=True, max_length = 25)
	usuario = models.ForeignKey(User, on_delete=models.CASCADE)
	url_img = models.URLField()

	def __unicode__(self):
		return u'%s %s %s' % (self.nombreImg, self.usuario, self.url_img)
