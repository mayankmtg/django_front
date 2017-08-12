from django.db import models

class Question(models.Model):
	question = models.CharField(max_length=1250)
	A = models.CharField(max_length=250)
	B = models.CharField(max_length=250)
	C = models.CharField(max_length=250)
	D = models.CharField(max_length=250)
	ans = models.CharField(max_length=3)
	skill1=models.CharField(max_length=250)
	skill2=models.CharField(max_length=250)
	# catagory = models.ForeignKey(Catagory, on_delete=models.CASCADE)

	def __str__(self):
		return self.question


class questionBank(models.Model):
	name = models.CharField(max_length=250)
	question1=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question1')
	question2=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question2')
	question3=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question3')
	question4=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question4')
	question5=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question5')
	question6=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question6')
	question7=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question7')
	question8=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question8')
	question9=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question9')
	question10=models.ForeignKey(Question, on_delete=models.CASCADE, related_name='question10')

	def __str__(self):
		return self.name


class Assessment(models.Model):
	link = models.CharField(max_length=250)
	name = models.CharField(max_length=250)
	desc=models.CharField(max_length=250)
	duration=models.IntegerField(default=30)
	positive=models.IntegerField(default=4)
	negative=models.IntegerField(default=-1)
	bank=models.ForeignKey(questionBank, on_delete=models.CASCADE)

	def __str__(self):
		return self.name
