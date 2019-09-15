from django.db import models
from sorl.thumbnail import ImageField
from ckeditor.fields import RichTextField

# Create your models here.

class Newsletter(models.Model):
    email = models.EmailField()


class ContactUs(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    website = models.CharField(max_length=200)
    message  = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Us'


class Blog(models.Model):
    title = models.CharField(max_length=50)
    image = ImageField()
    author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)
    content = RichTextField()

class Banner(models.Model):
    image = ImageField()
    intro = models.TextField()
    title = models.CharField(max_length=50)
    end_date = models.DateTimeField(blank=True)
    location = models.CharField(max_length=10)


