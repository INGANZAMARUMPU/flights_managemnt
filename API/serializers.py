from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
	class Meta:
		model = User
		fields = "__all__"

class CompagnieSerializer(serializers.ModelSerializer):
	class Meta:
		model = Compagnie
		fields = "__all__"

class AvionSerializer(serializers.ModelSerializer):
	class Meta:
		model = Avion
		fields = "__all__"

class AeroportSerializer(serializers.ModelSerializer):
	class Meta:
		model = Aeroport
		fields = "__all__"

class VolSerializer(serializers.ModelSerializer):
	class Meta:
		model = Vol
		fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reservation
		fields = "__all__"