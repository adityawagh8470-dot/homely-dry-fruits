from rest_framework import generics, permissions
from .models import Category, Product
from .serializers import (
    CategorySerializer,
    ProductSerializer,
    ProductCreateUpdateSerializer,
)


# ✅ 1) CATEGORY LIST API
class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.filter(is_active=True).order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [permissions.AllowAny]


# ✅ 2) PRODUCT LIST API (Farmley Home Products Page)
class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.filter(is_active=True).order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]


# ✅ 3) PRODUCT DETAIL API
class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = "pk"


# ✅ 4) ADMIN: CREATE PRODUCT (UPLOAD IMAGE)
class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = [permissions.IsAdminUser]


# ✅ 5) ADMIN: UPDATE PRODUCT (UPLOAD IMAGE)
class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductCreateUpdateSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = "pk"
