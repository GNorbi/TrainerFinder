from django.db import models
from datetime import datetime

class SportPlace:
	id = models.AutoField(primary_key=True)
	add_Date = models.DateTimeField(default=datetime.utcnow, blank = True)
	add_User = models.ForeignKey('SportPlaceInstance', on_delete=models.SET_NULL, null=True) #TODO USER
	
	ty = (
		('a', "Aerobic Center"),
		('y', "Yoga Center"),
		('d', "Dance Center"),
		('p', "Pilates Center"),
		('g', "Gym"),
		('f', "Fitness Center"),
		('t', "Athletic Center"),
		('w', "Wellnes Center"),
    	)

	typeOf = models.CharField(max_length=1, choices=ty, blank=True, default='a', help_text='Type')


	class Meta:
		verbose_name = "Sport Place"
		verbose_name_plural = "Sport Place"	

	def __str__(self):
		"""
		String for representing the Model object.
		"""
		return str(self.id).encode('UTF-8')

	def save(self, force_insert=False, force_update=False, *args, **kwargs):
		super(SportPlace, self).save(force_insert, force_update, *args, **kwargs)


class SportPlaceInstance:
	id = models.AutoField(primary_key=True)
	sportPlace = models.ForeignKey('SportPlace',on_delete=models.SET_NULL, null = True)
	latitude = models.DecimalField(max_digits=9, decimal_places=6)
	longitude = models.DecimalField(max_digits=9, decimal_places=6)


class SportCourse:
	id = models.AutoField(primary_key=True)

	type1 = (
		('a', 'Aerobic Cen'),
		('h', "2."),
    	)

	typeOf = models.CharField(max_length=1, choices=type1, blank=True, default='f', help_text='Hiba Allapot')





class SportCourseInstance:
	id = models.AutoField(primary_key=True)
	sportCourse = models.ForeignKey('SportCourse',on_delete=models.SET_NULL, null = True)
	sportPlace = models.ForeignKey('SportPlaceInstance', on_delete=models.SET_NULL, null = True)
	coach = models.ForeignKey('SportPlaceInstance', on_delete=models.SET_NULL, null=True) #TODO change to USER

	#egy bizonyos időpontban tartott edzés
	oneTimeEvent = models.ForeignKey('OneTimeEvent', on_delete=models.SET_NULL, null=True)

	#rendszeresen tartott edzés
	regularyEvent = models.ForeignKey('RegularyEvent', on_delete=models.SET_NULL, null=True)



class RegularyEvent:
	startDate = models.DateTimeField(default=datetime.utcnow, blank=True)
	endDate = models.DateTimeField(default=datetime.utcnow, blank=True)

class OneTimeEvent:

	startDate = models.DateTimeField(default=datetime.utcnow, blank=True)
	endDate = models.DateTimeField(default=datetime.utcnow, blank=True)

