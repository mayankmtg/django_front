from django.conf.urls import include, url
from . import views



urlpatterns = [
    #Home 
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    # url(r'^contact/$', views.contact, name='contact'),
    # url(r'^blog/$', views.blog, name='blog'),
    # url(r'^clientele/$', views.clientele, name='clientele'),
    # url(r'^joblisting/$', views.joblisting, name='joblisting'),
    # url(r'^media/$', views.media, name='media'),
    # url(r'^testimonials/$', views.testimonials, name='testimonials'),
]
