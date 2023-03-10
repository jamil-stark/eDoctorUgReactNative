from .models import UserAccount
from .serializers import UserAccountSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


# when using a viewset, we specify all crud functionalities
class AccountViewSet(viewsets.ViewSet):
    # retrieve all accounts
    def list(self, request):
        accounts = UserAccount.objects.all()
        serializer = UserAccountSerializer(accounts, many=True)
        return Response(serializer.data)

    # create an account
    def create(self, request):
        serializer = UserAccountSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # retrieve specicif account
    def retrieve(self, request, pk=None):
        all_accounts = UserAccount.objects.all()
        account = get_object_or_404(all_accounts, pk=pk)
        serializer = UserAccountSerializer(account)
        return Response(serializer.data)
    

    # update an account
    def update(self, request, pk=None):
        account = UserAccount.objects.get(pk=pk)
        serializer = UserAccountSerializer(account, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

    #delete account
    def destroy(self, request, pk=None):
        account = UserAccount.objects.get(pk=pk)
        account.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
