from django.db import models

# Create your models here.
class Movies(models.Model):
	# title: unique, variable character chain, 64 byte maximum size, non null.
	title = models.CharField(max_length=64, unique=True, null=False)

	# episode_nb: full, PRIMARY KEY.
	episode_nb = models.AutoField(primary_key=True)

	# opening_crawl: text, can be null, no size limit.
	opening_crawl = models.TextField(null=True, blank=True)

	# director: variable character chain, non null, 32 bytes maximum size.
	director = models.CharField(max_length=32, null=False)

	# producer: variable character chain, non null, 128 bytes maximum size.
	producer = models.CharField(max_length=128, null=False)

	# release_date: date (without time), non null.
	release_date = models.DateField(null=False)

	def __str__(self):
		return self.title