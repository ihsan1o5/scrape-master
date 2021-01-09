from rest_framework import serializers
from scrapmaster_dashboard.models import ExtraDetails


class ExtraDetailsListSerializer(serializers.ModelSerializer):
	"""docstring for ExtraDetailsListSerializer"""
	class Meta:
		model=ExtraDetails
		fields=['id', 'name', 'details', 'date']
		
