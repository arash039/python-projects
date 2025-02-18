from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import Sum

# Create your models here.

class CustomUser(AbstractUser):
	reputation = models.IntegerField(default=0)

	groups = models.ManyToManyField("auth.Group", related_name="customuser_set", blank=True)
	user_permissions = models.ManyToManyField("auth.Permission", related_name="customuser_set", blank=True)

	def update_reputation(self):
		upvotes = self.tips.aggregate(upvote_score=models.Count("upvotedby")).get("upvote_score", 0)
		downvotes = self.tips.aggregate(upvote_score=models.Count("downvotedby")).get("downvote_score", 0)

		self.reputation = (upvotes * 5) - (downvotes * 2)
		self.save()

	def can_downvote(self):
		return self.reputation >= 15
	def can_delete_tips(self):
		return self.reputation >= 30
	
class Tip(models.Model):
	content = models.TextField()
	author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name="tips")
	date = models.DateField(auto_now_add=True)
	upvotedby = models.ManyToManyField(CustomUser, related_name="upvoted_tips", blank=True)
	downvotedby = models.ManyToManyField(CustomUser, related_name="downvoted_tips", blank=True)

	def save(self, *args, **kwargs):
		super().save(*args, **kwargs)
		self.author.update_reputation()

	def delete(self, *args, **kwargs):
		super().delete(*args, **kwargs)
		self.author.update_reputation()
