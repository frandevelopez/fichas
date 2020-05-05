from django.contrib import admin
from .models import Client, Ficha, Color, Supplier, Leather, Lining, Hardware


admin.site.register(Client)
admin.site.register(Ficha)
admin.site.register(Color)
admin.site.register(Supplier)
admin.site.register(Leather)
admin.site.register(Lining)
admin.site.register(Hardware)


# Register your models here.
