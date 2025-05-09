from django import forms
from django.forms import TextInput
from django.contrib import admin
from django.utils import timezone
from .models import Food, Ingredient, FoodIngredient
from .models import FoodCategory, Expense, ExpenseCategory
from .models import IngredientCategory

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

class ExpenseAdminForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'category', 'amount', 'description', 'date']
        widgets = {
            'amount': TextInput(attrs={'type': 'number', 'step': '1'}),  # Remove spinner by using a plain text input
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

@admin.register(IngredientCategory)
class IngredientCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    form = IngredientAdminForm
    list_display = ('name', 'cost', 'unit', 'category')
    search_fields = ('name', 'category__name')
    list_filter = ('category',)

@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    search_fields = ('name',)

@admin.register(ExpenseCategory)
class ExpenseCategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Expense)
class ExpenseAdmin(admin.ModelAdmin):
    form = ExpenseAdminForm
    list_display = ('category', 'amount', 'description', 'date')
    list_filter = ('category', 'date')
    search_fields = ('category__name', 'description')
    fields = ('name', 'category', 'amount', 'description', 'date')

    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        if not obj:
            # Set the initial date to today's date when adding a new Expense
            form.base_fields['date'].initial = timezone.now().date()
        return form
