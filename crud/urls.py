from django.urls import path
from . import views

urlpatterns = [
    path('', views.departmentVeiw.as_view(),name='department'),
    path('<pk>/ddelete/', views.DepartDelete.as_view(),name="deletedepartment"),
    path('dadd/', views.DaddView.as_view(),name="adddepartment"),
    path('<id>/', views.index.as_view(),name='index'),
    path('<pk>/delete/', views.employeeDelete.as_view(),name="deleteEmployee"),
    path('<pk>/update/', views.eUpdate.as_view(),name="updateEmployee"),
    path('<id>/add/', views.EaddView.as_view(),name="addEmployee"),
]