from django.db import models

# Create your models here.


class Author(models.Model):
    """Model definition for MODELNAME."""

    # TODO: Define fields here
    name = models.CharField(
        max_length = 50
    )
    last_name = models.CharField(
        max_length = 50
    )
    nationality = models.CharField(
        max_length = 30
    )
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name + ' ' + self.last_name
    '''
    class Meta:
        """Meta definition for MODELNAME."""

        verbose_name = 'MODELNAME'
        verbose_name_plural = 'MODELNAMEs'

    
    '''    

