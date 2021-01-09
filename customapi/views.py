from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import ExtraDetailsListSerializer
from scrapmaster_dashboard.models import ExtraDetails
from rest_framework import permissions
from .permissions import IsOwner


# Create your views here.

class ExtraDetailsListCreateAPIView(ListCreateAPIView):

	serializer_class = ExtraDetailsListSerializer
	queryset = ExtraDetails.objects.all()
	permission_classes = (permissions.IsAuthenticated,)
	
	def perform_create(self, serializer):
		return serializer.save(user=self.request.user)
		
	def get_queryset(self):
		return self.queryset.filter(user=self.request.user)


class ExtraDetailsAPIView(RetrieveUpdateDestroyAPIView):

	serializer_class = ExtraDetailsListSerializer
	queryset = ExtraDetails.objects.all()
	permission_classes = (permissions.IsAuthenticated, IsOwner)
	lookup_field = "id"
	
	def perform_create(self, serializer):
		return serializer.save(user=self.request.user)
		
	def get_queryset(self):
		return self.queryset.filter(user=self.request.user)

