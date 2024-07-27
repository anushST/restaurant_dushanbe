"""Urls of api app."""
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework.routers import DefaultRouter

from .constants import API_VERSION
from .views import (CategoryViewSet, CartViewSet, CompanyInfoViewSet,
                    DishViewSet, OrderViewSet)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'dishes', DishViewSet)
router.register(r'carts', CartViewSet)
router.register(r'orders', OrderViewSet)
router.register(r'company_info', CompanyInfoViewSet)

urlpatterns = [
    path(f'{API_VERSION}/', include(router.urls)),
]

schema_view = get_schema_view(
   openapi.Info(
      title="Restaurant API",
      default_version='v1',
      description="Документация для приложения cats проекта Kittygram",
      # terms_of_service="URL страницы с пользовательским соглашением",
      contact=openapi.Contact(email="admin@kittygram.ru"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns += [
    path(f'{API_VERSION}/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0),
         name='schema-swagger-ui'),
    path(f'{API_VERSION}/redoc/', schema_view.with_ui('redoc',
         cache_timeout=0),
         name='schema-redoc'),
]
