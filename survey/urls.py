from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('results/(?P<survey_id>\d+)/', views.list_surveys, name='results'),
    url('submit/', views.new_survey, name='submit'),
    url('create/', views.create, name='create'),
]