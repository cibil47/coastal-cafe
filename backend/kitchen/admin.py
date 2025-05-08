from django import forms
from django.contrib import admin
from .models import Food, Ingredient, FoodIngredient, Category

class FoodAdminForm(forms.ModelForm):
    class Meta:
        model = Food
        fields = '__all__'
        widgets = {
            'price': forms.TextInput(attrs={'type': 'text'}),
        }

class IngredientAdminForm(forms.ModelForm):
    class Meta:
        model = Ingredient
        fields = '__all__'
        widgets = {
            'cost': forms.TextInput(attrs={'type': 'text'}),
        }

class FoodIngredientInline(admin.TabularInline):
    model = FoodIngredient
    extra = 1

@admin.register(Food)
class FoodAdmin(admin.ModelAdmin):
    form = FoodAdminForm
    list_display = ('name', 'price', 'category')
    search_fields = ('name',)
    list_filter = ('category',)
    autocomplete_fields = ['category']
    inlines = [FoodIngredientInline]

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    form = IngredientAdminForm
    list_display = ('name', 'cost')
    search_fields = ('name',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

