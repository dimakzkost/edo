from django.shortcuts import render, HttpResponseRedirect
from rest_framework import viewsets
# from rest_framework.response import Response
# from users.models import User
# from users.serializers import UserSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser
# from django.contrib import auth
# from users.forms import UserLoginForm
# from django.urls import reverse
from lk.models import lk
from lk.serializers import lkSerializer


class lkViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated, )
    queryset = lk.objects.all()
    # serializer_class = lkSerializer
    # lookup_field = 'user'


def lk(request):
    return render(request, 'lk.html')