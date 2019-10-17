from django.urls import path
from WarUnicorn import views

urlpatterns = [
    path('unicorns/', views.unicorn_list),
    path('unicorns/<int:pk>/', views.unicorn_detail),
    path('can_connect/', views.can_connect)
]
