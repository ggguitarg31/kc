from django.contrib import admin
from .models import Clothes, ClothesCategory, Tags, Qualities, Sizes

admin.site.register(Clothes)
admin.site.register(ClothesCategory)
admin.site.register(Tags)
admin.site.register(Qualities)
admin.site.register(Sizes)