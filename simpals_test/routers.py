from django.urls import path, include


urlpatterns = [
    path('', include('client_api.urls')),
]
