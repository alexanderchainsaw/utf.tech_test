from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from utf_tech.foods.selectors import food_list
from utf_tech.foods.serializers import FoodListSerializer


class FoodListApi(APIView):

    def get(self, request):
        serializer = FoodListSerializer(food_list(), many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
