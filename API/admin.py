from django.contrib import admin

from .models import *

admin.site.register(Compagnie)
admin.site.register(Avion)
admin.site.register(Aeroport)
admin.site.register(Vol)
admin.site.register(Reservation)
