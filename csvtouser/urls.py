from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    # path('upload/', views.uploadView),
    path('', views.addView.as_view()),
    path('userDetails/', views.userDetails.as_view()),
    # path("",include('crud.urls'))
]
