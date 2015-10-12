from django.contrib import admin
from main.models import Cereal, Manufacturer



class CerealAdmin(admin.ModelAdmin):
     list_display = ('cereal_name', 'manufacturer')


    

admin.site.register(Cereal)
admin.site.register(Manufacturer)
