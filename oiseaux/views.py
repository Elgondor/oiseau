from django.shortcuts import render
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from .models import *
from .serializers import *

# Create your views here.
class RegistryAPIView(generics.ListCreateAPIView):
    queryset = Registry.objects.all()
    serializer_class = RegistrySerializer

class PersonAPIView(generics.ListCreateAPIView):
    queryset = Person.objects.all()
    # serializer_class = PersonSerializer(queryset, many=True)
    serializer_class = PersonSerializer

    

class RegistryTwoAPIView(generics.ListAPIView):
    queryset = Registry.objects.all()
    serializer_class = RegistryListSerializer
    

class OcassionAPIView(generics.ListCreateAPIView):
    queryset = Ocassion.objects.all()
    serializer_class = OcassionSerializer

class SampleMessageTwoAPIView(generics.ListAPIView):
    
    serializer_class = SampleMessageSerializer

    def get_queryset(self):
        print(self.kwargs['ocassion'])
        try:
            ocassion_id = self.kwargs['ocassion']
            return Sample_Message.objects.filter(ocassion=ocassion_id)
        except Exception as e:
            raise ValidationError({'error': 'You need to send an integer'})
        