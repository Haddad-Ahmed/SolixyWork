from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
class Collection(models.Model):
    TYPE_CH = [
        ('AI', 'Album Images'),
        ('AV', 'Album Video'),
        ('S', 'Son'),
    ]
    type = models.CharField('type', max_length=30, choices=TYPE_CH)
    nom = models.CharField('nom', max_length=30)
    public = models.BooleanField('public', default=True)

# Create your models here.
