from django.db import models
from datetime import datetime
from realtors.models import Realtor

class Gallery(models.Model):

  title = models.CharField(max_length=200, blank=True)
  video = models.CharField(max_length=2000, blank=True)



  gallery_image = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.title

class Email(models.Model):
      email_name = models.CharField(max_length=100, null=True, blank=True)
      from_email = models.EmailField(max_length=100, null=True, blank=True)
      phone = models.CharField(max_length=100, null=True, blank=True)

      message = models.CharField(max_length=100, null=True, blank=True)

      document = models.FileField(upload_to='documents/', null=True, blank=True)


