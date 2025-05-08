from django.contrib import admin
from .models import Food, Ingredient, FoodIngredient, Category

class FoodIngredientInline(admin.TabularInline):
    model = FoodIngredient
    extra = 1

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
    autocomplete_fields = ['category']
    inlines = [FoodIngredientInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cost')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

