from django.shortcuts import render

# Create your views here.
# ecommerce/views.py
from datetime import datetime, timedelta
from rest_framework import serializers
from rest_framework import generics
from ecomapp.models import Customer, Product
from ecomapp.serializers import CustomerSerializer, ProductSerializer,TokenGenerationSerializer
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.utils import timezone
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework_simplejwt.views import TokenObtainPairView
now = timezone.now()
# accounts/views.py

from django.contrib.auth.models import User
from rest_framework import generics
from .serializers import UserSerializer

class UserRegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CustomerRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [IsAuthenticated]

class ProductListCreateView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        customer = Customer.objects.get(user=self.request.user)
        serializer.save(customer=customer)

class ProductRetrieveUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.is_actiii:
            # Check if the product was registered less than 2 months ago
            registration_date = instance.registrationDate
            two_months_ago = timezone.now() - timedelta(days=60)
            if registration_date > two_months_ago:
                raise serializers.ValidationError("Product cannot be deactivated yet. It has not been registered for 2 months.")


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = TokenGenerationSerializer

