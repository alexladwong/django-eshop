from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(Cart)
admin.site.register(Cartitems)

search_fields = ["name"]
# admin.site.register(Price)
