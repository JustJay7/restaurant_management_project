from rest_framework.views import APIView
from rest_framework.response import response
from rest_framework import status

from .models import Item
from .serializers import ItemSerializer

class ItemView(APIView):
    def get(self, request):
        items = Item.objects.all()
        serializer = ItemSerializer(items, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class MenuView(APIView):
    def get(self, request):
        data = [
            {"name": "Margherita Pizza", "description": "Tomato, mozzarella, basil", "price": 9.99},
            {"name": "Penne Arrabbiata", "description": "Spicy tomato sauce", "price": 11.50},
            {"name": "Tiramisu", "description": "Espresso-soaked ladyfingers", "price": 6.00},
        ]
        return Response(data, status=status.HTTP_200_OK)