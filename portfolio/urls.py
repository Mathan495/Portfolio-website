from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name="home"),
    path('details/', views.details_page,name="details"),
    path('projects/',views.projects_page,name="projects"),
    path('contact/',views.contact_page,name="contact")
]