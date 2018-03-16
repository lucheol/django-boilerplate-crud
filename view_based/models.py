from django.db import models

# Create your models here.


class Estado(models.Model):
    """Model definition for Estado."""

    NomeEstado = models.CharField('Nome do Estado', max_length=50)
    Sigla = models.CharField('Sigla do Estado', max_length=2)

    class Meta:
        """Meta definition for Estado."""

        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'

    def __str__(self):
        """Unicode representation of Estado."""
        return self.NomeEstado
