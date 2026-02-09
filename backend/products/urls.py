from django.urls import path
from .views import (
    CategoryListAPIView,
    ProductListAPIView,
    ProductDetailAPIView,
    ProductCreateAPIView,
    ProductUpdateAPIView,
)

from .views_cart import (
    CartAPIView,
    CartItemUpdateAPIView,
    CartItemDeleteAPIView,
    CartClearAPIView,
)

urlpatterns = [
    # ✅ Public APIs
    path("categories/", CategoryListAPIView.as_view(), name="category-list"),
    path("products/", ProductListAPIView.as_view(), name="product-list"),
    path("products/<int:pk>/", ProductDetailAPIView.as_view(), name="product-detail"),

    # ✅ Cart APIs
    path("cart/", CartAPIView.as_view(), name="cart"),
    path("cart/item/<int:item_id>/update/", CartItemUpdateAPIView.as_view(), name="cart-item-update"),
    path("cart/item/<int:item_id>/delete/", CartItemDeleteAPIView.as_view(), name="cart-item-delete"),
    path("cart/clear/", CartClearAPIView.as_view(), name="cart-clear"),

    # ✅ Admin APIs
    path("admin/products/create/", ProductCreateAPIView.as_view(), name="product-create"),
    path("admin/products/<int:pk>/update/", ProductUpdateAPIView.as_view(), name="product-update"),
]
