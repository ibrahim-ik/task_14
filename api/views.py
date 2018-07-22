# Your imports should be here
from rest_framework.generics import ListAPIView
from restaurants.models import Restaurant
from .serializers import RestaurabtListSerializer


# Complete me! I should be your APIListView
class RestaurantListView(ListAPIView):
	queryset = Restaurant.objects.all()
	serializer_class = RestaurabtListSerializer