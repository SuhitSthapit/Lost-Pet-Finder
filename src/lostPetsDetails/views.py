from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render
#from django.shortcuts import get_object or 404
from django.views import View
from django.views.generic import TemplateView, ListView
import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Stock
from .serializers import StockSerializer
import json
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

class LostPetListView(ListView):
	template_name = 'lostPetDetails/lostpet_list.html' 

	def get_queryset(self):
		#rint(self.kwargs)
		slug = self.kwargs.get("slug")
		if slug:
			queryset = LostPet.objects.filter(
				Q(type_pet__iexact=slug) |
				Q(type_pet__icontains=slug)	
				)
		else:
			queryset = LostPet.objects.all()
		
		return queryset  

import xml.etree.ElementTree as ET
#list all stocks or create a new one #stocks/FB
#class StockList (APIView):
	#def get(self, request):
		#r = requests.get('http://aip-rest.appspot.com/api/token/12673341')

		#assert response.status_code == 200

		#for repo in r.json():
    	#	print ('{}{}'.format(repo['studentName'],repo['value']))

		#stocks = Stock.objects.all()
		#serializer = StockSerializer(stocks)
		#return Response(serializer.data)
	
#	def post(self):
#		pass
#from .forms import SubmitAssign


