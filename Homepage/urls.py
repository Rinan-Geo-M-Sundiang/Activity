
from django.urls import path
from django.views.generic import TemplateView

from .views import *

urlpatterns = [

    path('', home, name='home'),
    path('projects/', ProjectListView.as_view(), name='projects'),
    path('project/<int:pk>/', ProjectDetailView.as_view(), name='project-detail'),
    path('project/new/', ProjectCreateView.as_view(), name='project-create'),
    path('project/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project-edit'),  # <--- Add this URL pattern
    path('project/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project-delete'),
    path('contact/', contact, name='contact'),
    path('inquiries/', inquiry_list, name='inquiry-list'),
    path('contact/', contact, name='contact'),
    path('thank-you/', TemplateView.as_view(template_name="thank_you.html"), name='thank-you'),

]