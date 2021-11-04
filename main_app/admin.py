from django.contrib import admin
from .models import Bird, Sighting
# Register your models here.
admin.site.register(Bird)
admin.site.register(Sighting)