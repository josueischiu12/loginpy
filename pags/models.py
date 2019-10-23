from django.db import models

# Create your models here.
class Paginas(models.Model):
    """Model definition for Paginas."""

    # TODO: Define fields here
    titulo = models.CharField(max_length=200)
    contenido = models.TextField()
    orden = models.SmallIntegerField(default=0)
    creado = models.DateTimeField(auto_now_add=True)
    editado = models.DateTimeField(auto_now_add=True)

    class Meta:
        """Meta definition for Paginas."""

        verbose_name = 'Pagina'
        verbose_name_plural = 'Paginas'
        ordering = ['orden', 'titulo']

    def __str__(self):
        """Unicode representation of Paginas."""
        return self.titulo
