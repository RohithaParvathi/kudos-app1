from rest_framework import viewsets
from .models import User, Kudos, Organization
from .serializers import UserSerializer, KudosSerializer, OrganizationSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class KudosViewSet(viewsets.ModelViewSet):
    queryset = Kudos.objects.all()
    serializer_class = KudosSerializer

class OrganizationViewSet(viewsets.ModelViewSet):
    queryset = Organization.objects.all()
    serializer_class = OrganizationSerializer
