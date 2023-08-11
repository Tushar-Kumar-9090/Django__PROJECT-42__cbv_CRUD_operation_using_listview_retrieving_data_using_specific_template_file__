from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from app.models import *


class School_list(ListView):
    model = School
    context_object_name = 'allSO'
    
    ## here defining the << template_name ='app/school_list.html' >> is option 
    ## when we define the specific template file means --> creating a folder inside template folder same as
    ## application name and inside this create a HTML file name --> modelsname_list.html
    ## at that time defining the template_name is not neccessary it will access automatically.  
    # template_name ='app/school_list.html'   


class Student_list(ListView):
    model = Student
    context_object_name = 'allStuObj'