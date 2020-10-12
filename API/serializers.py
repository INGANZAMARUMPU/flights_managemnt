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

	source = serializers.SerializerMethodField()
	destination = serializers.SerializerMethodField()
	avion = serializers.SerializerMethodField()
	compagnie = serializers.SerializerMethodField()

	def get_compagnie(self, obj):
		return f"{obj.avion.compagnie}"

	def get_avion(self, obj):
		return obj.avion.model

	def get_destination(self, obj):
		return obj.destination.ville

	def get_source(self, obj):
		return obj.source.ville
	
	class Meta:
		model = Vol
		fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
	nom = serializers.SerializerMethodField()
	prenom = serializers.SerializerMethodField()
	vol = serializers.SerializerMethodField()
	depart = serializers.SerializerMethodField()
	arrivee = serializers.SerializerMethodField()

	def get_nom(self, obj):
		return obj.user.first_name

	def get_prenom(self, obj):
		return obj.user.last_name

	def get_vol(self, obj):
		return f"{obj.vol.avion.compagnie}: {obj.vol.source.ville} to {obj.vol.destination.ville}"

	def get_depart(self, obj):
		return f"{obj.vol.depart}"
		
	def get_arrivee(self, obj):
		return f"{obj.vol.arrivee}"

	class Meta:
		model = Reservation
		fields = "__all__"