from django.db import models
from datetime import datetime

class Content(models.Model):

  title = models.CharField(max_length=200, blank=True)

  header_email = models.CharField(max_length=30, blank=True)
  header_phone = models.CharField(max_length=20, blank=True)

  bottom_content_one = models.CharField(max_length=200, blank=True)
  bottom_details_one = models.TextField(max_length=2000, null=True, blank=True)

  bottom_content_two = models.CharField(max_length=200, blank=True)
  bottom_details_two = models.TextField(max_length=2000, null=True, blank=True)

  bottom_content_three = models.CharField(max_length=200, blank=True)
  bottom_details_three = models.TextField(max_length=2000, null=True, blank=True)

  footer_facebook = models.CharField(max_length=200, blank=True)
  footer_twitter = models.CharField(max_length=200, blank=True)
  footer_instragram = models.CharField(max_length=200, blank=True)
  footer_linkedin = models.CharField(max_length=200, blank=True)
  footer_pinterest = models.CharField(max_length=200, blank=True)



  slider_photos_main = models.ImageField(upload_to='photos/%Y/%m/%d/',  blank=True)
  slider_photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  slider_photo_two = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  slider_photo_three = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_four = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_five = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  photo_six = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)
  def __str__(self):
    return self.title