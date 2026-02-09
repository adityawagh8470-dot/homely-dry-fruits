from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView




from users.permissions import IsAdminUserJWT
from products.models import Product, Category
from products.serializers import ProductSerializer, CategorySerializer
from orders.models import Order
from orders.serializers import OrderSerializer


class AdminProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all().order_by("-id")
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserJWT]


class AdminProductUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserJWT]


class AdminCategoryListCreateAPIView(generics.ListCreateAPIView):
    queryset = Category.objects.all().order_by("-id")
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserJWT]


class AdminCategoryUpdateDeleteAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserJWT]


class AdminOrderListAPIView(generics.ListAPIView):
    queryset = Order.objects.all().order_by("-id")
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated, IsAdminUserJWT]


class AdminOrderStatusUpdateAPIView(APIView):
    permission_classes = [permissions.IsAuthenticated, IsAdminUserJWT]

    def patch(self, request, pk):
        try:
            order = Order.objects.get(pk=pk)
        except Order.DoesNotExist:
            return Response({"error": "Order not found"}, status=status.HTTP_404_NOT_FOUND)

        new_status = request.data.get("status")
        valid_status = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]

        if new_status not in valid_status:
            return Response(
                {"error": f"Invalid status. Use: {valid_status}"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order.status = new_status
        order.save()

        return Response({"message": "Order status updated", "status": order.status})
