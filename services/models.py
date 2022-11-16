from distutils.command.upload import upload
from django.db import models

# Create your models here.
# Siempre se colocan los modelos en singular


class Service(models.Model):
    title = models.CharField(max_length=200, verbose_name="Título")
    subtitle = models.CharField(max_length=200, verbose_name="Subtítulo")
    image = models.ImageField(verbose_name="Imagen", upload_to="services")
    content = models.TextField(verbose_name="Contenido")
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(
        auto_now=True, verbose_name="Fecha de actualización")

    # Creamos una subclase - Poner atención a la identación
    class Meta:
        verbose_name = "servicio"
        verbose_name_plural = "servicios"
        # ordering = ['-created'] #Muestra desde el más actual hasta el más antigup
        ordering = ['created']  # Desde el mas antiguo hasta el mas actual

    def __str__(self):
        return self.title

  # Una vez creado el modelo, se coloca el nombre
  # de la aplicación en el comando makemigrations
