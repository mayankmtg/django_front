from django.db import models
from django.core.urlresolvers import reverse
from django.utils.crypto import get_random_string

class questionBank(models.Model):
	name = models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse('Assessment:wizardHome')

	def __str__(self):
		return self.name
class Skill(models.Model):
	questionBank=models.ForeignKey(questionBank, on_delete=models.CASCADE)
	skill=models.CharField(max_length=250)

	def get_absolute_url(self):
		return reverse('Assessment:wizardSkills')

	def __str__(self):
		return self.skill

class Question(models.Model):
	questionBank=models.ForeignKey(questionBank, on_delete=models.CASCADE)
	question = models.CharField(max_length=1250)
	A = models.CharField(max_length=250)
	B = models.CharField(max_length=250)
	C = models.CharField(max_length=250)
	D = models.CharField(max_length=250)
	ans = models.CharField(max_length=3)
	skill1=models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill1')
	skill2=models.ForeignKey(Skill, on_delete=models.CASCADE, related_name='skill2')

	def get_absolute_url(self):
		return reverse('Assessment:wizardQuestions')
	def __str__(self):
		return self.question




class Assessment(models.Model):
	id=models.AutoField(primary_key=True)
	link = models.CharField(max_length=250, blank=True, default='',unique=True )
	name = models.CharField(max_length=250)
	desc=models.CharField(max_length=250)
	duration=models.IntegerField(default=30)
	positive=models.IntegerField(default=4)
	negative=models.IntegerField(default=-1)
	bank=models.ForeignKey(questionBank, on_delete=models.CASCADE)
	
	def save(self, force_insert=False, force_update=False):
		self.link = get_random_string(length=32)
		super(Assessment, self).save(force_insert, force_update)

	def get_absolute_url(self):
		return reverse('Assessment:create')

	def __str__(self):
		return self.name

class Result(models.Model):
	user_name=models.CharField(max_length=250)
	user_id=models.CharField(max_length=250)
	total_score=models.IntegerField(default=0)
	current_score=models.IntegerField(default=0)