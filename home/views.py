from django.shortcuts import render
from .models import Job
from django.contrib.auth.decorators import login_required
# class based views
from django.views.generic import ListView, UpdateView, DetailView, CreateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin

# Create your views here.
def welcome(request):
    return render(request, "home/homepage.html")


class JobListView(ListView):
    model = Job
    template_name = "home/jobs.html"
    context_object_name = 'ctx'
    ordering = ["-posted_on", ]


class JobDescView(DetailView):
    model = Job


@login_required
def jobs(request):
    context = Job.objects.all()
    return render(request, "home/jobs.html", {'ctx': context})


class CreateJob(LoginRequiredMixin,CreateView):
    model = Job
    fields = ["occupation", 'posts', 'sector', 'organization', 'mode', 'description', 'deadline', 'Location']

    # setting the currenly logged in user to the post being written
    def form_valid(self, form):
        form.instance.poster = self.request.user
        return super().form_valid(form)

class UpdateJob(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model = Job
    fields = ['occupation','posts','mode','deadline','Location']
    def test_func(self):
        post = self.get_object()
        if self .request.user == post.poster:
            return True
        else:
            return False
class DeleteJob(LoginRequiredMixin,UserPassesTestMixin, DeleteView):
    model = Job
    # this test func ensures that only the once
    def test_func(self):
        post = self.get_object()
        if self .request.user == post.poster:
            return True
        else:
            return False
    success_url = "/"



