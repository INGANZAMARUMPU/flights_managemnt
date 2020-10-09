from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register("user", UserViewset)
router.register("compagnie", CompagnieViewset)
router.register("avion", AvionViewset)
router.register("aeroport", AeroportViewset)
router.register("vol", VolViewset)
router.register("reservation", ReservationViewset)

urlpatterns = [
	path("", include(router.urls)),
]
