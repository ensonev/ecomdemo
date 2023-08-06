from django.shortcuts import render
from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response
from .models import Product, User
from .serializers import CustomerSerializers, ProductSerializers
from django.utils import timezone
from datetime import  timedelta

class CustomerViewSet(viewsets.ModelViewSet):
    """
       staff user details
       ******************
        username:admin 
        password:admin
        note: customer's username and password are same. (should be changed in real contexts)
        """
    serializer_class = CustomerSerializers
    queryset = User.objects.all()
    permission_classes = (IsAdminUser,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializers
    queryset = Product.objects.all()
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': self.request})
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  

    def update(self, request, *args, **kwargs):
        obj = self.get_object()
        serializer = ProductSerializers(obj, data=request.data)
        if serializer.is_valid():
            if not bool(request.data.get('active')):
                inactive_time_period = obj.created_at + timedelta(days=60)
                if not timezone.now() > inactive_time_period:
                    return Response({'message': f"Sorry you can change the status after {inactive_time_period}"
                                     }, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 