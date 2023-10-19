from django.http import JsonResponse
from .models import Restapi
from .serializers import RestapiSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET', 'POST'])
def restapi_list(request, format=None):
  if request.method == 'GET':
      restapis = Restapi.objects.all()
      serializer = RestapiSerializer(restapis, many=True)
      return Response(serializer.data)
    
  if request.method == 'POST':
      serializer = RestapiSerializer(data=request.data)
      if serializer.is_valid():
          serializer.save()
          return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def restapi_detail(request ,id, format=None):

  try:
    restapi = Restapi.objects.get(pk=id)
  except Restapi.DoesNotExist:
    return Response(status=status.HTTP_404_NOT_FOUND)

  if request.method == 'GET':
    serializer = RestapiSerializer(restapi)
    return Response(serializer.data)
  elif request.method == 'PUT':
    serializer = RestapiSerializer(restapi, data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'DELETE':
    restapi.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

