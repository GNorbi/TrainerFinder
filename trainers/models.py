from django.db import models
from datetime import datetime

class SportPlace:
	id = models.AutoField(primary_key=True)
	add_Date = models.DateTimeField(default=datetime.utcnow, blank = True)
	add_User = models.ForeignKey('User', on_delete=models.SET_NULL, null=True)

	typeOf = models.CharField(max_length=1, choices=type, blank=True, default='f', help_text='Hiba Allapot')

	type = (
		('g', 'Gym'),
		('h', "2."),
    	)


	def save(self, force_insert=False, force_update=False, *args, **kwargs):
		super(SportPlace, self).save(force_insert, force_update, *args, **kwargs)


class SportPlaceInstance:
	id = models.AutoField(primary_key=True)
	sportCourse = models.ForeignKey('SportPlace',on_delete=models.SET_NULL, null = True)



class SportCourse:
	id = models.AutoField(primery_key=True)

	typeOf = models.CharField(max_length=1, choices=type, blank=True, default='f', help_text='Hiba Allapot')

	type = (
		('g', 'Gym'),
		('h', "2."),
    	)


class SportCourseInstance:
	id = models.AutoField(primary_key=True)
	sportCourse = models.ForeignKey(SportCourse,on_delete=models.SET_NULL, null = True)

	#egy bizonyos időpontban tartott edzés
	oneTimeEvent = models.ForeignKey(OneTimeEvent, on_delete=models.SET_NULL, null=True)

	#rendszeresen tartott edzés
	regularyEvent = models.ForeignKey(RegularyEvent, on_delete=models.SET_NULL, null=True)


	coach = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)


class RegularyEvent:
	day1 = models.BooleanField(initial=False)
	startTime1 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime1 = models.TimeField(_(u"Conversation Time"), blank=True)

	day2 = models.BooleanField(initial=False)
	startTime2 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime2 = models.TimeField(_(u"Conversation Time"), blank=True)
	
	day3 = models.BooleanField(initial=False)
	startTime3 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime3 = models.TimeField(_(u"Conversation Time"), blank=True)
	
	day4 = models.BooleanField(initial=False)
	startTime4 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime4 = models.TimeField(_(u"Conversation Time"), blank=True)
	
	day5 = models.BooleanField(initial=False)
	startTime5 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime5 = models.TimeField(_(u"Conversation Time"), blank=True)
	
	day6 = models.BooleanField(initial=False)
	startTime6 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime6 = models.TimeField(_(u"Conversation Time"), blank=True)
	
	day7 = models.BooleanField(initial=False)
	startTime7 = models.TimeField(_(u"Conversation Time"), blank=True)
	endTime7 = models.TimeField(_(u"Conversation Time"), blank=True)

class OneTimeEvent:

	startDate = models.DateTimeField(default=datetime.utcnow, blank=True)
	endDate = models.DateTimeField(default=datetime.utcnow, blank=True)

# Create your models here.
