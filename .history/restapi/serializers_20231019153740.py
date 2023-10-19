from rest_framework import serializers
from .models import Restapi

class RestapiSerializer(serializers.ModelSerializer):
  class Meta:
    model = Restapi
    fields = ['id', 'name', 'description']
    