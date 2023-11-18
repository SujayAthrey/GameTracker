from rest_framework import serializers
from .models import Gametracker

class GametrackerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Gametracker
        fields = ('id','title','description','completed')
