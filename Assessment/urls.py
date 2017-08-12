from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login

app_name='Assessment'

urlpatterns = [
    #Home 
    url(r'^$', views.assessmentView.as_view(), name='assessment'),
    url(r'^auth/$', views.assessmentAuth.as_view(), name='auth'),
    url(r'^wizard/(?P<wiz_page>\w+)/$', views.assessmentWizard, name='wizard'),
    url(r'^create/$', views.assessmentCreate.as_view(), name='create'),

    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^blog/$', views.blog, name='blog'),
    # url(r'^clientele/$', views.clientele, name='clientele'),
    # url(r'^joblisting/$', views.joblisting, name='joblisting'),
    # url(r'^media/$', views.media, name='media'),
    # url(r'^testimonials/$', views.testimonials, name='testimonials'),
]
