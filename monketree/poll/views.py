from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from poll.models import User
from poll.serializer import UserSerializer


# Create your views here.


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
