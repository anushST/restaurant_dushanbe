"""Main views of the api app."""
from rest_framework import viewsets
from rest_framework.filters import SearchFilter
from rest_framework.mixins import CreateModelMixin

from ..serializers import (CategorySerializer, CompanyInfoSerializer,
                           DishSerializer, OrderSerializer)
from order.models import Order
from product.models import Category, Dish
from restaurant.models import CompanyInfo


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    """Category viewset."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'

    def get_queryset(self):
        """Return queryset to work with."""
        queryset = super().get_queryset()
        filters = self.request.query_params.get('filters')
        if filters:
            filters_list = filters.split(',')
            for filter in filters_list:
                if filter == 'main':
                    queryset = queryset.filter(is_on_main=True)
        return queryset


class CompanyInfoViewSet(viewsets.ReadOnlyModelViewSet):
    """Comapny info viewset."""

    queryset = CompanyInfo.objects.all()
    serializer_class = CompanyInfoSerializer
    pagination_class = None


class DishViewSet(viewsets.ReadOnlyModelViewSet):
    """Dish viewset."""

    queryset = Dish.objects.all()
    serializer_class = DishSerializer
    filter_backends = (SearchFilter,)
    search_fields = ('name',)

    def get_queryset(self):
        """Return queryset to work with."""
        queryset = super().get_queryset()
        filters = self.request.query_params.get('filters')
        category = self.request.query_params.get('category')
        if category:
            queryset = queryset.filter(categories__slug=category)
        if filters:
            filters_list = filters.split(',')
            for filter in filters_list:
                if filter == 'main':
                    queryset = queryset.filter(is_on_main=True)
                if filter == 'new':
                    queryset = queryset.filter(is_new=True)
        return queryset


class OrderViewSet(CreateModelMixin, viewsets.GenericViewSet):
    """Order viewset."""

    queryset = Order.objects.all()
    serializer_class = OrderSerializer
