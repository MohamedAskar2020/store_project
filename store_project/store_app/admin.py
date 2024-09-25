# store_app/admin.py

from django.contrib import admin
from .models import Category, Product, Offer, ShoppingCart, CartProduct, Order, ReturnOrder, PaymentMethod, Payment, CustomUser

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Offer)
admin.site.register(ShoppingCart)
admin.site.register(CartProduct)
admin.site.register(Order)
admin.site.register(ReturnOrder)
admin.site.register(PaymentMethod)
admin.site.register(Payment)
admin.site.register(CustomUser)

