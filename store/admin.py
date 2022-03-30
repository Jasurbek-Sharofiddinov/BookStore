from django.contrib import admin
from .models import Book,User,Order,OrderItem,Category

# Register your models here.
admin.site.register(Book)
admin.site.register(User)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(Category)
