from django.db import models
from django.conf import settings
from datetime import datetime

User = settings.AUTH_USER_MODEL
# Model to store the list of logged in users
class LoggedInUser(models.Model):
    user = models.OneToOneField(User, related_name='logged_in_user', on_delete=models.CASCADE)
    # Session keys are 32 characters long
    session_key = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.user.username

class Poll(models.Model):
	question = models.TextField()
	option_one = models.CharField(max_length=30)
	option_two = models.CharField(max_length=30)
	option_three = models.CharField(max_length=30)
	option_four = models.CharField(max_length=30)
	option_one_count = models.IntegerField(default=0)
	option_two_count = models.IntegerField(default=0)
	option_three_count = models.IntegerField(default=0)
	option_four_count = models.IntegerField(default=0)


	def total(self):
		return self.option_one_count + self.option_two_count + self.option_three_count + self.option_four_count

	class Meta:
		verbose_name_plural = "Polls"




class TutorialCategory(models.Model):
	tutorial_category = models.CharField(max_length=200)
	category_summary = models.CharField(max_length=200)
	category_slug = models.CharField(max_length=200, default=1)

	class Meta:
		verbose_name_plural = "Categories"

	def __str__(self):
		return self.tutorial_category

class TutorialSeries(models.Model):
	tutorial_series = models.CharField(max_length=200)
	tutorial_category = models.ForeignKey(TutorialCategory, default = 1, verbose_name="Category", on_delete=models.CASCADE)
	series_summary = models.CharField(max_length=200)

	class Meta:
		verbose_name_plural = "Series"

	def __str__(self):
		return self.tutorial_series

# Create your models here.
class Tutorial(models.Model):
	tutorial_title = models.CharField(max_length=200)
	tutorial_content = models.TextField()
	tutorial_published = models.DateTimeField("date published", default=datetime.now)
	tutorial_series = models.ForeignKey(TutorialSeries, default = 1, verbose_name="Series", on_delete=models.CASCADE)
	tutorial_slug = models.CharField(max_length=200, default=1)


	def __str__(self):
		return self.tutorial_title