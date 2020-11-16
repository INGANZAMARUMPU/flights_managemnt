from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from .serializers import *
from .models import *

class UserViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = UserSerializer
	queryset = User.objects.all()

class CompagnieViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication,]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = CompagnieSerializer
	queryset = Compagnie.objects.all()

class AvionViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication,]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = AvionSerializer
	queryset = Avion.objects.all()

class AeroportViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication,]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = AeroportSerializer
	queryset = Aeroport.objects.all()

class VolViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = VolSerializer
	queryset = Vol.objects.all()

class ReservationViewset(viewsets.ModelViewSet):
	authentication_classes = [SessionAuthentication, TokenAuthentication]
	permission_classes = [IsAuthenticatedOrReadOnly, ]
	serializer_class = ReservationSerializer
	queryset = Reservation.objects.all()

class CustomAuthToken(ObtainAuthToken):
	def post(self, request, *args, **kwargs):
		user = authenticate(**request.data)
		if(user is not None):
			token, created = Token.objects.get_or_create(user=user)
			group = "" if not user.groups.all() else user.groups.all()[0].name
			return Response({
				'token': token.key,
				'group': group
			})
		return Response({})