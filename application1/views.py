from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,TemplateView,DetailView,CreateView,UpdateView,DeleteView
from application1.models import *
from django.urls import reverse_lazy
class SchoolList(ListView):
    model=School
    context_object_name='schools'
    # template_name='application1/school_list.html'
    # ordering=['ScName']
    #queryset=School.objects.filter(ScName='SAIECM')
class home(TemplateView):
    template_name='application1\home.html'
class SchoolDetails(DetailView):
    model=School
    context_object_name='schoolobject'
class SchoolCreate(CreateView):
    model=School
    fields='__all__'
class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'
class SchoolDelete(DeleteView):
    model=School
    context_object_name='sclobj'
    success_url=reverse_lazy('SchoolList')
class StudentInsert(CreateView):
    model=Student
    fields='__all__'
    success_url=reverse_lazy('SchoolList')


