from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from WarUnicorn import views

urlpatterns = [
    path("unicorns/", views.UnicornList.as_view()),
    path("unicorns/<int:pk>/", views.UnicornDetail.as_view()),
    path("can_connect/", views.CanConnect.as_view()),
]


urlpatterns = format_suffix_patterns(urlpatterns)
