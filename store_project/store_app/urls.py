# store_app/urls.py

from django.urls import path
from .views import ReviewListCreateView, UserRegistrationView, CategoryListView, ProductListView, ShoppingCartView, OrderListView, LogoutView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework_simplejwt.views import TokenBlacklistView


urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('categories/', CategoryListView.as_view(), name='categories'),
    path('products/', ProductListView.as_view(), name='products'),
    path('cart/', ShoppingCartView.as_view(), name='cart'),
    path('orders/', OrderListView.as_view(), name='orders'),
    path('products/<int:product_id>/reviews/', ReviewListCreateView.as_view(), name='product-reviews'),
]
