from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from api.v1.views import (DashboardViewSet, LevelViewSet, LibraryViewSet,
                          MyUsersViewSet, ShortUserSkillViewSet, SkillDetail,
                          SkillViewSet, UserActivationView, UserSkillViewSet)

app_name = "v1"

api_info = openapi.Info(
    title="Skills API",
    default_version="v1",
    description="Документация для проекта Skills",
)

schema_view = get_schema_view(
    public=True,
    permission_classes=[permissions.AllowAny],
)

router_v1 = DefaultRouter()
router_v1.register("users", MyUsersViewSet, basename="users")
router_v1.register("userskills", UserSkillViewSet, basename="userskills")
router_v1.register("levels", LevelViewSet, basename="level")
router_v1.register("dashboard", DashboardViewSet, basename="dashboard")
router_v1.register("libraries", LibraryViewSet, basename="library")
router_v1.register(
    "short-userskills",
    ShortUserSkillViewSet,
    basename="short-userskills")


urlpatterns = [
    re_path(
        r"activate/(?P<uid>[\w-]+)/(?P<token>[\w-]+)/$",
        UserActivationView.as_view(),
    ),
    path("", include(router_v1.urls)),
    path("", include("djoser.urls.base")),
    path("auth/", include("djoser.urls.jwt")),
    path('skills/', SkillViewSet.as_view({'get': 'list'})),
    path('skills/<int:pk>/', SkillDetail.as_view()),
]

urlpatterns += [
    path(
        "swagger<format>/",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
