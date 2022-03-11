from rest_framework import serializers
from .models import wallpeps


class wallpepsSerialiser(serializers.ModelSerializer):
  
  #image = serializers.ImageField(max_length=None, use_url=True)
  class Meta:
    model = wallpeps
    fields = '__all__'