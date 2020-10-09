from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Compagnie(models.Model):
	nom = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.nom}"

class Avion(models.Model):
	compagnie = models.ForeignKey("Compagnie", on_delete=models.CASCADE)
	model = models.CharField(max_length=16)

	def __str__(self):
		return f"{self.model} - {self.compagnie}"

class Aeroport(models.Model):
	nom = models.CharField(max_length=64)
	ville = models.CharField(max_length=32)

	def __str__(self):
		return f"{self.nom} - {self.ville}"

class Vol(models.Model):
	date = models.DateTimeField(default=timezone.now)
	avion = models.ForeignKey("Avion", on_delete=models.PROTECT)
	source = models.ForeignKey("Aeroport", related_name='source', on_delete=models.PROTECT)
	destination = models.ForeignKey("Aeroport", related_name='destination', on_delete=models.PROTECT)

	def __str__(self):
		return f"{self.source} -> {self.destination} à {self.date}"

class Reservation(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	vol = models.ForeignKey(Vol, on_delete=models.CASCADE)

	def __str__(self):
		return f"{self.user.firstname} {self.vol}"
