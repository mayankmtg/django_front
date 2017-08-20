from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login

app_name='Assessment'

urlpatterns = [
    #Home 
    url(r'^$', views.assessmentView.as_view(), name='assessment'),
    url(r'^auth/$', views.assessmentAuth.as_view(), name='auth'),
    url(r'^wizard/home/$', views.assessmentWizardHome.as_view(), name='wizardHome'),
    url(r'^wizard/skills/$', views.assessmentWizardSkills.as_view(), name='wizardSkills'),
    url(r'^wizard/questions/$', views.assessmentWizardQuestions.as_view(), name='wizardQuestions'),
    url(r'^wizard/questions/(?P<pk>[0-9]+)/$', views.assessmentWizardQuestionsDetail.as_view(), name='wizardQuestionsDetail'),
    url(r'^wizard/questionbank/$', views.assessmentWizardBank.as_view(), name='wizardBank'),
    url(r'^wizard/questionbank/(?P<bank_id>[0-9]+)/$', views.assessmentWizardBankDetail, name='wizardBankDetail'),
    url(r'^create/home$', views.assessmentCreateHome.as_view(), name='createHome'),
    url(r'^create/createAssessment$', views.assessmentCreateAssessment.as_view(), name='createAssessment'),
    url(r'^create/assessment/(?P<pk>[0-9]+)/$', views.assessmentCreateDetail.as_view(), name='assessmentCreateDetail'),

    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^blog/$', views.blog, name='blog'),
    # url(r'^clientele/$', views.clientele, name='clientele'),
    # url(r'^joblisting/$', views.joblisting, name='joblisting'),
    # url(r'^media/$', views.media, name='media'),
    # url(r'^testimonials/$', views.testimonials, name='testimonials'),
]
