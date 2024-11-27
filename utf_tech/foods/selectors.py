from django.db.models.query import QuerySet
from utf_tech.foods.models import FoodCategory, Food
from django.db.models import Prefetch


def food_list() -> QuerySet[FoodCategory]:
    published_food_qs = Food.objects.filter(is_publish=True)

    food_categories_qs = (
        FoodCategory.objects
        .filter(food__is_publish=True)
        .distinct()
        .prefetch_related(Prefetch('food', queryset=published_food_qs))
        .order_by('id')
        .all()
    )

    return food_categories_qs
