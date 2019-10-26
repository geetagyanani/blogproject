from django.db import models
from django.utils import timezone
class Services(models.Model):
	title = models.CharField(max_length=255)
	updated_at = models.DateTimeField('created',default=timezone.now)
	image = models.CharField(max_length=255,default='')
	created_at = models.DateTimeField('created',default=timezone.now)
	status = models.CharField(max_length=30 , default = 'publish')
class Partners(models.Model):
	title = models.CharField(max_length=255)
	updated_at = models.DateTimeField('created',default=timezone.now)
	image = models.CharField(max_length=255,default='')
	created_at = models.DateTimeField('created',default=timezone.now)
	status = models.CharField(max_length=30 , default = 'publish')
class Products(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(default='')
	updated_at = models.DateTimeField('created',default=timezone.now)
	image = models.CharField(max_length=255,default='')
	created_at = models.DateTimeField('created',default=timezone.now)
	status = models.CharField(max_length=30 , default = 'publish')
class Sliders(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(default='')
	updated_at = models.DateTimeField('created',default=timezone.now)
	image = models.CharField(max_length=255,default='')
	created_at = models.DateTimeField('created',default=timezone.now)
	status = models.CharField(max_length=30 , default = 'publish')
class Homeservices(models.Model):
	title = models.CharField(max_length=255)
	description = models.TextField(default='')
	updated_at = models.DateTimeField('created',default=timezone.now)
	image = models.CharField(max_length=255,default='')
	created_at = models.DateTimeField('created',default=timezone.now)
	status = models.CharField(max_length=30 , default = 'publish')
	readmore_link = models.CharField(max_length=255,default='')

	



# Create your models here.
