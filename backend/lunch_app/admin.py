from django.contrib import admin
from .models import (Ingredient, Recipe, RecipeImage, RecipeItem, Storage, StorageItem)

# Register your models here.
admin.site.register(Ingredient)
admin.site.register(Recipe)
admin.site.register(RecipeImage)
admin.site.register(RecipeItem)
admin.site.register(StorageItem)
admin.site.register(Storage)
