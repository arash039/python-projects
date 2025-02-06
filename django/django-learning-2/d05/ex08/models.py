from django.db import models

class Planets(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True)
	climate = models.CharField(max_length=128)
	diameter = models.IntegerField()
	orbital_period = models.IntegerField()
	population = models.BigIntegerField()
	rotation_period = models.IntegerField()
	surface_water = models.FloatField()
	terrain = models.CharField(max_length=128)

	def __str__(self):
		return self.name

class People(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=64, unique=True)
	birth_year = models.CharField(max_length=32)
	gender = models.CharField(max_length=32)
	eye_color = models.CharField(max_length=32)
	hair_color = models.CharField(max_length=32)
	height = models.IntegerField()
	mass = models.FloatField()
	homeworld = models.ForeignKey(Planets, to_field="name", on_delete=models.CASCADE)

	def __str__(self):
		return self.name
