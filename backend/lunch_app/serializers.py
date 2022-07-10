from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import (Ingredient, Recipe, RecipeImage,
                     RecipeItem, StorageItem, Storage)


class IngredientSerializer(serializers.HyperlinkedModelSerializer):
    # TODO:add list of recipeItems
    class Meta:
        model = Ingredient
        fields = ['url', 'id', 'name']


class RecipeItemIdentityField(serializers.HyperlinkedIdentityField):
    def to_representation(self, value):
        return reverse('recipe-item-detail', kwargs={'recipe_pk': value.recipe.id, 'pk': value.id}, request=self.context['request'])


class RecipeItemListIdentityField(serializers.HyperlinkedIdentityField):
    def to_representation(self, value):
        return reverse('recipe-item-list', kwargs={'recipe_pk': value.id}, request=self.context['request'])


class RecipeImageIdentityField(serializers.HyperlinkedIdentityField):
    def to_representation(self, value):
        return reverse('recipe-image-detail', kwargs={'recipe_pk': value.recipe.id, 'pk': value.id}, request=self.context['request'])


class RecipeImageListIdentityField(serializers.HyperlinkedIdentityField):
    def to_representation(self, value):
        return reverse('recipe-image-list', kwargs={'recipe_pk': value.id}, request=self.context['request'])


class RecipeSerializer(serializers.HyperlinkedModelSerializer):
    # TODO:add list of items
    item_list = RecipeItemListIdentityField('recipe-item-list', read_only=True)
    image_list = RecipeImageListIdentityField(
        'recipe-image-list', read_only=True)

    class Meta:
        model = Recipe
        fields = ['url', 'id', 'title', 'date_created',
                  'estimated_prep_time', 'difficulty', 'item_list', 'image_list']


class RecipeItemSerializer(serializers.HyperlinkedModelSerializer):
    url = RecipeItemIdentityField(view_name='recipe-item-detail')
    recipe = serializers.HyperlinkedRelatedField(
        'recipe-detail', many=False, queryset=Recipe.objects.all())
    ingredient = serializers.HyperlinkedRelatedField(
        'ingredient-detail', many=False, queryset=Ingredient.objects.all())

    class Meta:
        model = RecipeItem
        fields = ['url', 'id', 'amount', 'amount_type', 'recipe', 'ingredient']


class RecipeImageSerializer(serializers.HyperlinkedModelSerializer):
    url = RecipeImageIdentityField('recipe-image-detail')
    recipe = serializers.HyperlinkedRelatedField(
        'recipe-detail', many=False, queryset=Recipe.objects.all())

    class Meta:
        model = RecipeImage
        fields = ['url', 'id', 'title', 'is_highlight', 'recipe']


class StorageSerializer(serializers.HyperlinkedModelSerializer):
    # TODO:add list of items
    class Meta:
        model = Storage
        fields = ['url', 'id', 'name']


class StorageItemSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField('storage-item-detail')
    ingredient = serializers.HyperlinkedRelatedField(
        'ingredient-detail', many=False, queryset=Ingredient.objects.all())
    storage = serializers.HyperlinkedRelatedField(
        'storage-detail', many=False, queryset=Storage.objects.all())

    class Meta:
        model = StorageItem
        fields = ['url', 'id', 'due_date']
