from django.urls import path
from .views import (
    AdminProductListCreateAPIView,
    AdminProductUpdateDeleteAPIView,
    AdminCategoryListCreateAPIView,
    AdminCategoryUpdateDeleteAPIView,
    AdminOrderListAPIView,
    AdminOrderStatusUpdateAPIView,
)

urlpatterns = [
    # PRODUCTS (CRUD)
    path("products/", AdminProductListCreateAPIView.as_view()),
    path("products/<int:pk>/", AdminProductUpdateDeleteAPIView.as_view()),

    # CATEGORIES (CRUD)
    path("categories/", AdminCategoryListCreateAPIView.as_view()),
    path("categories/<int:pk>/", AdminCategoryUpdateDeleteAPIView.as_view()),

    # ORDERS
    path("orders/", AdminOrderListAPIView.as_view()),
    path("orders/<int:pk>/status/", AdminOrderStatusUpdateAPIView.as_view()),
]
