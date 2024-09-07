from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from .models import Project
from .forms import ContactForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from .models import Contact
def home(request):
    return render(request, 'home.html', {} )


class ProjectListView(ListView):
    model = Project
    template_name = 'project_list.html'  # <app>/<model>_<viewtype>.html
    context_object_name = 'projects'
    ordering = ['-date_posted']

class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project_detail.html'



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank-you')  # Redirect to a 'thank you' page after successful form submission
        else:
            # Even if the form is invalid, we need to return the form with errors
            return render(request, 'contact.html', {'form': form})
    else:
        # On a GET request, render a blank form
        form = ContactForm()
        return render(request, 'contact.html', {'form': form})

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['title', 'description', 'image', 'project_url']


class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['title', 'description', 'image', 'project_url']

    def test_func(self):
        return self.request.user.is_superuser


class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser

@login_required
def inquiry_list(request):
    inquiries = Contact.objects.all()
    return render(request, 'inquiry_list.html', {'inquiries': inquiries})

# Create your views here.
