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
	compagnie = serializers.SerializerMethodField()

	def get_compagnie(self, obj):
		return f"{obj.avion.compagnie}"

	def to_representation(self, obj):
		representation = super().to_representation(obj)
		representation['source'] = obj.source.ville
		representation['destination'] = obj.destination.ville
		representation['avion'] = obj.avion.model
		return representation
	
	class Meta:
		model = Vol
		fields = "__all__"

class ReservationSerializer(serializers.ModelSerializer):
	nom = serializers.SerializerMethodField()
	prenom = serializers.SerializerMethodField()
	depart = serializers.SerializerMethodField()
	arrivee = serializers.SerializerMethodField()

	def get_nom(self, obj):
		return obj.user.first_name

	def get_prenom(self, obj):
		return obj.user.last_name

	def get_depart(self, obj):
		return obj.vol.depart
		
	def get_arrivee(self, obj):
		return obj.vol.arrivee

	def to_representation(self, obj):
		representation = super().to_representation(obj)
		representation['vol'] = f"{obj.vol.avion.compagnie}: {obj.vol.source.ville} to {obj.vol.destination.ville}"
		return representation

	class Meta:
		model = Reservation
		fields = "__all__"
