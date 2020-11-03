from rest_framework import generics, filters, permissions
from django.contrib.postgres.search import SearchQuery, SearchVector, SearchRank
from django_filters.rest_framework import DjangoFilterBackend
from . import models
from .permissions import IsOwnerProfileOrReadOnly
from . import serializers


#API for ordering in Advert model
class OrderAdverts(generics.ListAPIView):
    queryset = models.UserAdverts.objects.all()
    serializer_class = serializers.AdvertsFilterDataSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['name']


#API for searching in Advert model
class SearchFor(generics.ListAPIView):

    serializer_class = serializers.AdvertsFilterDataSerializer
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'user__username', 'city__name', 'body']
    ordering_fields = ['name']

    def get_queryset(self):
        vector = SearchVector('name', 'user__username', 'city__name','body')
        query = SearchQuery(self.request.GET.get("search"))

        return models.UserAdverts.objects.annotate(rank=SearchRank(vector, query))


#API for filter Advert model
class AdvertsFilter(generics.ListAPIView):
    queryset = models.UserAdverts.objects.all()
    serializer_class = serializers.AdvertsFilterDataSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user', 'city']


#API for getting all users
class UserDataListCreateView(generics.ListCreateAPIView):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserDataSerializer

    def perform_create(self, serializer):
        user = self.request.user
        serializer.save(user = user)


#API for getting user details
class userDataDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserData.objects.all()
    serializer_class = serializers.UserDataSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, permissions.IsAuthenticated]


class CityView(generics.ListCreateAPIView):
    queryset = models.Cities.objects.all()
    serializer_class = serializers.CityDataSerializer
    permission_classes = [permissions.IsAdminUser]


class CityDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Cities.objects.all()
    serializer_class = serializers.CityDataSerializer
    permission_classes = [permissions.IsAdminUser]


class AdvertsListCreateView(generics.ListCreateAPIView):
    queryset = models.UserAdverts.objects.all()
    serializer_class = serializers.AdvertsDataSerializer

    def perform_create(self, serializer):
        user = self.request.user
        print(user)
        serializer.save(user = user)


class AdvertsDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.UserAdverts.objects.all()
    serializer_class = serializers.AdvertsDataSerializer
    permission_classes = [IsOwnerProfileOrReadOnly, permissions.IsAuthenticated]

