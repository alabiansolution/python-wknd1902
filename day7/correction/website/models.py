from django.db import models
from tinymce import HTMLField
from fontawesome.fields import IconField

# Create your models here.

class AboutModel(models.Model):
    title = models.CharField(max_length=100, default='Default service')
    img = models.FileField(blank=True, null=True, default='Default service')
    description = HTMLField('Content', default='Default service')

    def __str__(self):
        return self.title

class ServiceModel(models.Model):
    service_title = models.CharField(max_length=100, default='Default service')
    icon = IconField(default='Default service')
    service_desc  = HTMLField('Content', default='Default service')

    def __str__(self):
        return self.service_title
