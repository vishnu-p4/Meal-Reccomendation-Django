from django.contrib import admin

# Register your models here.


from .models import Meals, Disease

admin.site.register(Meals)
admin.site.register(Disease)
