from rest_framework import generics
from rest_framework.response import Response
from .models import (Ingredient, Recipe, RecipeImage,
                     RecipeItem, StorageItem, Storage)
from .serializers import (IngredientSerializer, RecipeSerializer,
                          RecipeImageSerializer, RecipeItemSerializer, StorageItemSerializer, StorageSerializer)


class IngredientList(generics.ListCreateAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class IngredientDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ingredient.objects.all()
    serializer_class = IngredientSerializer


class RecipeList(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer


class RecipeImageList(generics.ListCreateAPIView):
    queryset = RecipeImage.objects.all()
    serializer_class = RecipeImageSerializer


class RecipeImageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecipeImage.objects.all()
    serializer_class = RecipeImageSerializer


class RecipeItemList(generics.ListCreateAPIView):
    serializer_class = RecipeItemSerializer

    def get_queryset(self):
        recipe_pk = self.kwargs['recipe_pk']
        return RecipeItem.objects.filter(recipe=recipe_pk)


class RecipeItemDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = RecipeItemSerializer

    def get_queryset(self):
        recipe_pk = self.kwargs['recipe_pk']
        return RecipeItem.objects.filter(recipe=recipe_pk)


class StorageList(generics.ListCreateAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = Storage.objects.all()
    serializer_class = StorageSerializer


class StorageItemList(generics.ListCreateAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer


class StorageItemDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset = StorageItem.objects.all()
    serializer_class = StorageItemSerializer
