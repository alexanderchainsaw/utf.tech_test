from django.urls import include, path

urlpatterns = [
    path('foods/', include(("utf_tech.foods.urls", "foods")))
]
