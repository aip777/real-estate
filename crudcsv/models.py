from django.db import models
from django.core.validators import RegexValidator
from datetime import datetime

# Create your models here.
# class Member(models.Model):
#     firstname = models.CharField(max_length=40, blank=False)
#     lastname = models.CharField(max_length=40, blank=False)
#     mobile_number = models.CharField(max_length=10, blank=True)
#     description = models.TextField(max_length=255, blank=False)
#     date = models.DateField('%m/%d/%Y')
#     created_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
#     updated_at = models.DateTimeField('%m/%d/%Y %H:%M:%S')
#
# class Document(models.Model):
#     description = models.CharField(max_length=100, null=True, blank=True)
#     document = models.CharField(max_length=100, null=True, blank=True)
#     uploaded_at = models.DateTimeField(default=datetime.now, blank=True)
#
#     def __str__(self):
#         return self.document
#
# class Ajax(models.Model):
#     text = models.CharField(max_length=255, blank=True)
#     search = models.CharField(max_length=255)
#     email = models.EmailField(max_length=254)
#     telephone = models.CharField(max_length=10, blank=True)
#     created_at = models.DateTimeField()
#     updated_at = models.DateTimeField()

class CsvUpload(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    description = models.CharField(max_length=100, null=True, blank=True)
    end_date = models.DateTimeField(default=datetime.now, null=True, blank=True)
    notes = models.CharField(max_length=100, null=True, blank=True)
    images = models.ImageField(upload_to='photos', null=True, blank=True)

    def __str__(self):
        return self.name
