from django.contrib import admin

# Register your models here.
from .models import LostPet 
from .models import Stock 


admin.site.register(LostPet)

admin.site.register(Stock)