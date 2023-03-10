from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets, mixins
from django.shortcuts import get_object_or_404


class AccountViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    #queryset should strictly be used here || we cant use any other variable name so far 
    queryset = UserAccount.objects.all()
    serializer_class = UserAccountSerializer

    #when using genericviewsets, you have to sepecify the mixins to use

#GENERICVIEWSETS & ROUTERS