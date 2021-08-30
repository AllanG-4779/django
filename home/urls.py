from django.urls import path

from .views import JobListView,welcome,JobDescView, CreateJob,UpdateJob,DeleteJob
urlpatterns = [
      path('', welcome, name="starting"),
      path('jobs/', JobListView.as_view(), name='see-jobs'),
      path('job/<int:pk>/',JobDescView.as_view(),name="jobdesc" ),
      path("create/job", CreateJob.as_view(), name='jobcreate'),
      path("edit/job<int:pk>/",UpdateJob.as_view(), name="edit-job"),
      path("delete/job<int:pk>/",DeleteJob.as_view(), name="del-job"),

]

