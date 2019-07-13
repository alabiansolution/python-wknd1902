from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=100)
    cat_desc = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.cat_name

class Post(models.Model):
    post_title = models.CharField(max_length=100)
    post_img = models.FileField(blank=True, null=True)
    post_content = models.TextField(default='eiueuwhuywweueue')
    user = models.ForeignKey('auth.user')
    category = models.ManyToManyField(Category)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.post_title


class ContactModel(models.Model):
    REFERER_FIELD = [
        ('facebook','Facebook'),
        ('twitter','Twitter'),
        ('linkedin','Linkedin'),
        ('nairaland','Nairaland')
    ]
    GENDER_FIELD = [
        ('male','Male'),
        ('female','Female'),
    ]

    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=25)
    referer = models.CharField(max_length=50, choices=REFERER_FIELD)
    gender = models.CharField(max_length=20, choices=GENDER_FIELD)
    message = models.TextField()


    def __str__(self):
        return self.name
