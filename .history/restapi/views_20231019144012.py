from django.http import JsonResponse
from .models import Restapi
from .serializers import RestapiSerializer

def restapi_list(request):
  restapis = Restapi.objects.all()
  serializer = RestapiSerializer(restapis, many=True)
  return JsonResponse(serializer.data)
  