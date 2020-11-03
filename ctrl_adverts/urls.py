from django.urls import path
from . import views


urlpatterns = [
    # gets all user profiles and create a new profile
    path("accounts/all-profiles/", views.UserDataListCreateView.as_view(), name="all-profiles"),
    # retrieves profile details of the currently logged in user
    path("accounts/profile/<int:pk>/", views.userDataDetailView.as_view(), name="profile"),

    #get all cities from model
    path("accounts/all-cities/", views.CityView.as_view(), name="all-cities"),
    #retrieves city name
    path("accounts/city/<int:pk>/", views.CityDetailView.as_view(), name="city-detail"),

    # get all adverts from model
    path("accounts/all-adverts/", views.AdvertsListCreateView.as_view(), name="all-adverts"),
    # retrieves advert detail
    path("accounts/advert/<int:pk>/", views.AdvertsDetailView.as_view(), name="advert-detail"),

    #get user list filter
    path("filter/adverts", views.AdvertsFilter.as_view(), name="adverts-filter"),

    #url for search adverts
    path("search/", views.SearchFor.as_view(), name="search"),

    #url for order adverts
    path("order/", views.OrderAdverts.as_view(), name="order"),
]