from django.urls import path
from . import views

urlpatterns = [
    path('ingredients/', views.IngredientList.as_view(), name='ingredient-list'),
    path('ingredients/<int:pk>/', views.IngredientDetails.as_view(),
         name='ingredient-detail'),
    path('recipes/', views.RecipeList.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', views.RecipeDetails.as_view(), name='recipe-detail'),
    # TODO: fix *Item views
    path('recipes/<int:recipe_pk>/items/',
         views.RecipeItemList.as_view(), name='recipe-item-list'),
    path('recipes/<int:recipe_pk>/items/<int:pk>/',
         views.RecipeItemDetails.as_view(), name='recipe-item-detail'),
    path('recipes/<int:recipe_pk>/images/',
         views.RecipeImageList.as_view(), name='recipe-image-list'),
    path('recipes/<int:recipe_pk>/images/<int:pk>/',
         views.RecipeImageDetails.as_view(), name='recipe-image-detail'),
    path('storages/', views.StorageList.as_view(), name='storage-list'),
    path('storages/<int:pk>/', views.StorageDetails.as_view(), name='storage-detail'),
    # path('storages/<int:storage_pk>/items/',
    #      views.RecipeList.as_view(), name='storage-item-list'),
    # path('storages/<int:storage_pk>/items/<int:item_pk>/',
    #      views.RecipeDetails.as_view(), name='storage-item-detail'),
]
