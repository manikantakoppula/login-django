from django.shortcuts import render
from django.views.generic import ListView,DeleteView,DetailView
from .models import UserFile ,UserInfo
from django.views.generic.edit import UpdateView,CreateView
from .forms import AddForm
from django.views.generic.base import TemplateView,View
from .service import someFunction
# Create your views here.




class userDetails(ListView):
    model = UserInfo
    template_name = 'csvtouser/basic.html' 
    def get_queryset(self):
        try:
            path = UserFile.objects.get(status=0)
            someFunction(path)
            print(path)
        except:
            print("error")
        users = UserInfo.objects.all()
        return users
        
    
class uploadView(View):
    
    pass

class addView(CreateView):
    form_class = AddForm
    template_name = 'csvtouser/add.html'
    success_url = 'userDetails/'
    

