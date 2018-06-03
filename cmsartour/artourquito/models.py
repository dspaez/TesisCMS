from django.db import models

class MonumentosQuito(models.Model):
    mid = models.CharField(max_length=200)
    nombre_monumento = models.CharField(max_length=200)
    descripcion_monumento = models.TextField(max_length=2000)
    latitud = models.CharField(max_length=50)
    longitud = models.CharField(max_length=50)
    imagen_antigua = models.ImageField(upload_to='imagenes/')
    def __str__(self):
        return self.nombre_monumento
    def image_tag(self):
    	return u'<img src="%s" />' %imagen_antigua.url
    	image_tag.short_description = 'imagen_antigua'
    	image_tag.allow_tags = True