from rest_framework import serializers
from .models import User, Kudos, Organization

class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class KudosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kudos
        fields = '__all__'
