from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from kudos.views import UserViewSet, KudosViewSet, OrganizationViewSet

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('kudos', KudosViewSet)
router.register('organizations', OrganizationViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
]
