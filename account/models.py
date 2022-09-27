
from django.db import models
from django.template.defaultfilters import slugify
from django.utils import timezone
from uuid import uuid4
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *
from account.models import *
from django_countries.fields import CountryField
from cloudinary.models import CloudinaryField





# Create your models here.
class CountryNames(models.Model):
    country = CountryField(blank=True)

    def __str__(self):
        return self.country



class PartnersDetails(models.Model):
    user = models.OneToOneField(User, on_delete= models.SET_NULL,related_name='partners',null=True)
    uniqueId = models.CharField(null=True, blank=True, max_length=100)
    dateRegistered =models.DateTimeField(auto_now_add=True, null=True)
    country = CountryField(blank=True)
    phone = models.CharField(max_length=50,null=True)
    profile_img = CloudinaryField(blank=True,null=True)
    dateRegistered =models.DateTimeField(auto_now_add=True, null=True)
    date_created = models.DateTimeField(blank=True, null=True)
    slug = models.SlugField(max_length=100, unique=True, blank=True, null=True)
    last_updated = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name_plural='PartnersDetails'


    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        if self.date_created is None:
            self.date_created = timezone.localtime(timezone.now())

        if self.uniqueId is None:
            self.uniqueId = str(uuid4()).split('-')[4]
            self.slug = slugify('{} {}'.format(self.user, self.uniqueId))

        self.slug = slugify('{} {}'.format(self.user, self.uniqueId))
        self.last_updated = timezone.localtime(timezone.now())

        super(PartnersDetails, self).save(*args, **kwargs)    

