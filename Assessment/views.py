from django.shortcuts import render
from django.views import generic


class assessmentView(generic.TemplateView):
	template_name = 'Assessment/assessment.html'

class assessmentCreate(generic.TemplateView):
	template_name = "Assessment/create.html"

class assessmentAuth(generic.TemplateView):
	template_name = "Assessment/auth.html"


def assessmentWizard(request,wiz_page ):
	context={
		'wiz_page': wiz_page,
	}
	return render(request, 'Assessment/wizard.html', context)