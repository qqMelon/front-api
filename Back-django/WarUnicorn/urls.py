from django.urls import path
from WarUnicorn import views
from rest_framework_simplejwt import views as jwt_views
from django.conf.urls import url, include
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)

# import ipdb; ipdb.set_trace()
urlpatterns = [
    url(r"^", include(router.urls)),
    url(r"^auth/", include("rest_auth.urls")),
    path("unicorns/", views.UnicornList.as_view(), name="unicorns_list"),
    path("unicorns/<int:pk>/", views.UnicornDetail.as_view(), name="unicorn_detail"),
    path("can_connect/", views.CanConnect.as_view()),
    path("login/", views.LoginView.as_view(), name="login"),
    path("token/", jwt_views.TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("token/refresh/", jwt_views.TokenRefreshView.as_view(), name="token_refresh"),
]
