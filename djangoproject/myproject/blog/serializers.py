from rest_framework import serializers
from .models import Addblog

class Addblogserializer(serializers.ModelSerializer):


    class Meta:
        model = Addblog
        fields = ['title','blog','date']  #__all__