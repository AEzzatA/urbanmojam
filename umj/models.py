import datetime
from django.db import models
from django.utils import timezone
# Create your models here.

#TODO:
#1 Change Definition class name it doesn't look good
#2 Change meaning name to meaning and Field to TextField() not char field
#3

class Term(models.Model):
	'''
	Term/Phrase model. that needs to be defined
	phrase -> CharField
	pub_date -> DateTimeField
	'''
	phrase =  models.CharField(max_length = 140)
	pub_date = models.DateTimeField('date added')

	def __unicode__(self):
		return self.phrase
	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
	was_published_recently.admin_order_field = 'pub_date'
	was_published_recently.boolean = True
	was_published_recently.short_description = 'Published Recently?'


class Definition(models.Model):
	''' Term definition
	term -> CharField
	country -> CharField | country code
	'''
	term = models.ForeignKey(Term)
	meaning = models.TextField()
	votes = models.IntegerField(default=0)
	counrty_list = (
		('DZ', 'Algeria'),
		('BH', 'Bahrain'),
		('TD', 'Chad'),
		('KM', 'Comoros'),
		('DJ', 'Djibouti'),
		('EG', 'Egypt'),
		('ER', 'Eritrea'),
		('IQ', 'Iraq'),
		('JO', 'Jordan'),
		('KW', 'Kuwait'),
		('LB', 'Lebanon'),
		('LY', 'Libya'),
		('MR', 'Mauritania'),
		('MA', 'Morocco'),
		('OM', 'Oman'),
		('PS', 'Palestine'),
		('QA', 'Qatar'),
		('EH', 'SADR'),
		('SA', 'Saudi Arabia'),
		('SO', 'Somalia'),
		('SD', 'Sudan'),
		('SY', 'Syria'),
		('TN', 'Tunisia'),
		('AE', 'United Arab Emirates'),
		('YE', 'Yemen')
		)
	country = models.CharField(max_length=2,
		choices=counrty_list,
		default='EG')

	pub_date = models.DateTimeField('date added definition')

	def __unicode__(self):
		return "{0} {1}".format(self.meaning, self.country)

	def was_published_recently(self):
		return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Tag(models.Model):
	''' Tags that realates to term definition'''
	terms = models.ManyToManyField(Term)
	tag_name = models.CharField(max_length=15)
