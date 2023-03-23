from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DeleteView,DetailView
from django.views.generic.edit import UpdateView,CreateView
from .forms import AddForm,AddDepartForm
from .models import Employee ,Department
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.mixins import PermissionRequiredMixin ,LoginRequiredMixin
from django.contrib import messages

class departmentVeiw(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = ("crud.view_department")
    model = Department
    template_name = 'crud/deplist.html'
    
    def get_queryset(self):
        department = Department.objects.all()
        return department

class index(LoginRequiredMixin,PermissionRequiredMixin,ListView):
    permission_required = "crud.view_employee"
    model = Employee
    template_name = 'crud/elist.html'
    def get_queryset(self):
        employees = Employee.objects.filter(department__pk=self.kwargs['id'])
        return employees

class employeeDelete(LoginRequiredMixin,PermissionRequiredMixin,DeleteView):
    permission_required = "crud.delete_employee"
    model = Employee
    template_name = "crud/delete.html"
    success_url = '/index/'

class eUpdate(LoginRequiredMixin,PermissionRequiredMixin,UpdateView):
    template_name = "crud/eupdate.html"
    model = Employee
    form_class = AddForm
    permission_required = "crud.change_employee"
    success_url = '/index/'

class EaddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "crud.add_employee"
    form_class = AddForm
    template_name = 'crud/add.html'
    success_url = '/index/'
    # permission_required = "crud.add_department"


class DaddView(LoginRequiredMixin,PermissionRequiredMixin,CreateView):
    permission_required = "crud.add_department"
    form_class = AddDepartForm
    template_name = 'crud/dadd.html'
    success_url = '/index/'

class DepartDelete(PermissionRequiredMixin,DeleteView):
    model = Department
    template_name = "crud/delete.html"
    permission_required = "crud.delete_department"
    permission_denied_message = 'You are not allowed this transaction!! Ha Ha!!'
    success_url ="/index/"
    login_url ='/login/'
    