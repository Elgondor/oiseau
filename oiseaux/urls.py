from django.urls import path
from .views import *
urlpatterns = [
    path("registry", RegistryAPIView.as_view(), name="registry_list"),
    path("person", PersonAPIView.as_view(), name="registry_list"),
    path("registrytwo", RegistryTwoAPIView.as_view(), name="registry_list"),
    path("ocassion", OcassionAPIView.as_view(), name="ocassion_list"),
    path("sample_message/<ocassion>", SampleMessageTwoAPIView.as_view(), name="sample_message_list"),
]