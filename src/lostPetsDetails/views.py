from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView

from .models import LostPet 

class HomeView(TemplateView):
    template_name = "home.html"
class ContactView(TemplateView):
    template_name = "contact.html"
   
# class AboutView(TemplateView):
#     template_name = "about.html"

def lostPet_listview(request):
	template_name = 'lostPetDetails/lostpet_list.html' 
	queryset = LostPet.objects.all()
	context = {"object_list": queryset}
	return render(request,template_name,context)