from rest_framework import serializers
from .models import *

# class GiftSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Gift
#         fields = ("amount", "art_id", "note", "accepted", "registry",)

class RegistrySerializer(serializers.ModelSerializer):
    # gifts = GiftSerializer(many=True, required=False)
    
    class Meta:
        model = Registry
        fields = ("ocassion", "registry_title", "name", "event_date", "message",
                  "registry_link", "show_who_sent_gifts", "dark_mode", "photo", "gifts")
        
class RegistryListSerializer(serializers.ModelSerializer):
    gifts = serializers.StringRelatedField(many = True)
    class Meta:
        model = Registry
        fields = ("id", "registry_title", "event_date", "gifts")
        
class OcassionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocassion
        fields = ("name", "art")

class SampleMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sample_Message
        fields = ("comment", "ocassion")
        