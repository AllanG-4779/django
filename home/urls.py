from django.urls import  path

from . import views

urlpatterns = [
      path('', views.welcome, name="starting" ),
      path('jobs/', views.jobs, name='see-jobs')

]
