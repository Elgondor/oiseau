from rest_framework import serializers
from .models import *

# class GiftSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gift
#         fields = ("amount", "art_id", "note", "accepted", "registry",)

class RegistryCUSerializer(serializers.ModelSerializer):
    class Meta:
        model = Registry
        fields = ("ocassion", "registry_title", "persons", "event_date", "message",
                  "registry_link", "show_who_sent_gifts", "dark_mode", "photo_url", "gifts")
        
class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ("name", "last_name", "registry")
        
class RegistryListSerializer(serializers.ModelSerializer): 
    gifts = serializers.StringRelatedField(many = True)
    class Meta:
        model = Registry
        fields = ("id", "registry_title", "event_date", "gifts", "photo_url")
        
class OcassionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocassion
        fields = ("title", "art")

class SampleMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample_Message
        fields = ("comment", "ocassion")


        