from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Skill, Question, questionBank, Assessment


class assessmentView(generic.TemplateView):
	template_name = 'Assessment/assessment.html'

class assessmentCreateHome(generic.ListView):
	template_name = "Assessment/create/home.html"
	def get_queryset(self):
		# the returned queryset is in the variable object_list
		return Assessment.objects.all()
class assessmentCreateDetail(generic.DetailView):
	model=Assessment
	template_name="Assessment/create/detail.html"

class assessmentCreateAssessment(CreateView):
	model = Assessment
	fields=['name','desc','duration','positive','negative','bank']
	template_name = "Assessment/create/createAssessment.html"

class assessmentAuth(generic.TemplateView):
	template_name = "Assessment/auth.html"

class assessmentWizardHome(generic.ListView):
	template_name = "Assessment/wizard/home.html"
	def get_queryset(self):
		# the returned queryset is in the variable object_list
		return questionBank.objects.all()

def assessmentWizardBankDetail(request, bank_id):
	cur_bank=questionBank.objects.get(pk=bank_id)
	req_skills=cur_bank.skill_set.all()
	req_ques=cur_bank.question_set.all()
	context = {
		'cur_bank':cur_bank,
		'req_skills': req_skills,
		'req_ques': req_ques,
	}
	return render(request, 'Assessment/wizard/bankDetail.html',context )


class assessmentWizardBank(CreateView):
	model = questionBank
	fields=['name']
	template_name = "Assessment/wizard/questionbank.html"

class assessmentWizardQuestions(CreateView):
	model = Question
	fields = ['questionBank','question','A','B','C','D','ans','skill1','skill2']
	template_name = "Assessment/wizard/questions.html"

class assessmentWizardQuestionsDetail(generic.DetailView):
	model = Question
	template_name = "Assessment/wizard/questionDetail.html"

class assessmentWizardSkills(CreateView):
	model = Skill
	fields = ['questionBank', 'skill']
	template_name = "Assessment/wizard/skills.html"

class assessmentWizardAssignSkill(generic.TemplateView):
	template_name = "Assessment/wizard/assignskills.html"
