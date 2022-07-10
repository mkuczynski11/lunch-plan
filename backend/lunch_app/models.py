from django.db import models
from enum import Enum

# Create your models here.


class AmountEnum(Enum):
    G = 1
    KG = 2


class Ingredient(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    # TODO: add image for an ingredient
    # image =
    # TODO: add information about macros???

    def __str__(self) -> str:
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    date_created = models.DateTimeField(
        auto_now_add=True, blank=False, null=False)
    estimated_prep_time = models.IntegerField()
    difficulty = models.FloatField(
        choices=[(str(float(i)*0.5), float(i)*0.5) for i in range(2, 11)])

    def __str__(self) -> str:
        return self.title


# TODO:fix id generation to be dependent on recipe
class RecipeItem(models.Model):
    amount = models.IntegerField(null=False, blank=False)
    # TODO: add more choices
    amount_type = models.CharField(max_length=50,
                                   choices=[(e, e) for e in AmountEnum._member_names_], blank=False, null=False)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.recipe} : {self.ingredient}'


# TODO:fix id generation to be dependent on recipe
class RecipeImage(models.Model):
    title = models.CharField(max_length=100, null=False, blank=False)
    is_highlight = models.BooleanField()
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.recipe} : {self.title}'


class Storage(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    
    def __str__(self) -> str:
        return self.name


# TODO:fix id generation to be dependent on storage
class StorageItem(models.Model):
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    # TODO: make abstract class AmountItem for StorageItem and RecipeItem to inherit from
    amount = models.IntegerField(null=False, blank=False)
    # TODO: add more choices
    amount_type = models.CharField(max_length=50,
                                   choices=[(e, e) for e in AmountEnum._member_names_], blank=False, null=False)
    due_date = models.DateTimeField()

    def __str__(self) -> str:
        return f'{self.storage} : {self.ingredient}'
