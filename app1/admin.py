from django.contrib import admin
from .models import CustomUser, Organization, Report, Product

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Organization)
admin.site.register(Report)
admin.site.register(Product)
