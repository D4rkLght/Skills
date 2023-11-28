from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (SkillViewSet, UserSkillViewSet)

app_name = 'api'

router = DefaultRouter()
router.register('skills', SkillViewSet)
router.register('user-skills', UserSkillViewSet)
#router.register('stores', StoreShortViewSet)
#router.register('stores-with-products', StoreLongViewSet)
#router.register('chains', ChainStoreViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
