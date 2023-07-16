from django.urls import path


# accounts/urls.py

from django.urls import path
from .views import UserRegisterView,LoginView,CustomerListCreateView,CustomerRetrieveUpdateDeleteView,ProductListCreateView,ProductRetrieveUpdateDeleteView

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('customers/', CustomerListCreateView.as_view(), name='customer-list'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDeleteView.as_view(), name='customer-list'),
    path('Product/', ProductListCreateView.as_view(), name='customer-list'),
    path('Product/<int:pk>/',ProductRetrieveUpdateDeleteView.as_view(), name='customer-list'),
]