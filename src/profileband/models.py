from django.db import models
from datetime import datetime

class Profileband(models.Model):



  title_one = models.CharField(max_length=200, blank=True)
  name_one = models.CharField(max_length=200, blank=True)
  email_address = models.CharField(max_length=200, blank=True)
  phone_number = models.CharField(max_length=200, blank=True)
  summary_text_one = models.TextField(max_length=2000, null=True, blank=True)
  profile_facebook_one = models.CharField(max_length=200, blank=True)
  profile_twitter_one = models.CharField(max_length=200, blank=True)
  profile_instragram_one = models.CharField(max_length=200, blank=True)
  profile_linkedin_one = models.CharField(max_length=200, blank=True)
  profile_photo_one = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)





  is_published = models.BooleanField(default=True)
  list_date = models.DateTimeField(default=datetime.now, blank=True)

  def __str__(self):
    return self.name_one