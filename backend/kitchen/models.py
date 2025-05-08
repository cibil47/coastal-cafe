from django.db import models

class Ingredient(models.Model):
    name = models.CharField(max_length=50)
    cost = models.IntegerField(help_text="Cost per unit (in whole currency units)")

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name

class Food(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    ingredients = models.ManyToManyField(
        Ingredient,
        through='FoodIngredient',
        blank=True,
        related_name='foods'
    )

    def __str__(self):
        return self.name

    def estimated_cost(self):
        """Calculate estimated cost based on ingredients."""
        return sum(
            item.ingredient.cost * item.quantity
            for item in self.ingredient_links.all()
        )

class FoodIngredient(models.Model):
    food = models.ForeignKey(Food, on_delete=models.CASCADE, related_name='ingredient_links')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, help_text="Quantity of this ingredient used")

    class Meta:
        unique_together = ('food', 'ingredient')

    def __str__(self):
        return f"{self.quantity}x {self.ingredient.name} in {self.food.name}"
