from django.urls import path

from .apis import FoodListApi

urlpatterns = [path("", FoodListApi.as_view(), name="food_list")]
