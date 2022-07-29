from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from web.serializers import UserSerializer, GroupSerializer, NameSerializer
from web.models import Name
from rest_framework import generics

def index(request):
    return HttpResponse("Hello BRIDGERS!.")

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]   

class NameViewSet(viewsets.ModelViewSet):
    print("YEAH!")
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Name.objects.all()
    serializer_class = NameSerializer
    lookup_field = 'text'
#    permission_classes = [permissions.IsAuthenticated]       
