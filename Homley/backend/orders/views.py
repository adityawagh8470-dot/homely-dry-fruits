from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status, generics
from products.models import Cart, Product

from .models import Order, OrderItem
from .serializers import OrderSerializer


# ===============================
# PLACE ORDER API
# ===============================
class PlaceOrderAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        data = request.data
        items = data.get("items", [])

        if not items:
            return Response(
                {"error": "No items provided"},
                status=status.HTTP_400_BAD_REQUEST
            )

        order = Order.objects.create(user=user)
        total = 0
        
        # We need to map product names (from frontend) to Product IDs (in backend)
        # However, frontend sends names. Best to lookup by name or assume frontend can send IDs later.
        # For now, let's lookup by name as frontend JS sends 'name'.
        
        for item in items:
            product_name = item.get("name")
            qty = item.get("qty", 1)
            # Frontend price might change, so fetching from DB is safer, 
            # but for simplicity/speed let's trust DB price if product found.
            
            try:
                product = Product.objects.get(name__iexact=product_name)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=qty,
                    price=product.price
                )
                total += product.price * qty
            except Product.DoesNotExist:
                # If product not found, we skip or error? 
                # Let's skip safely or log
                print(f"Product {product_name} not found")
                continue

        order.total_amount = total
        order.save()

        return Response(
            {
                "message": "Order placed successfully",
                "order_id": order.id
            },
            status=status.HTTP_201_CREATED
        )


# ===============================
# USER ORDERS API
# ===============================
class UserOrdersAPIView(generics.ListAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Order.objects.filter(
            user=self.request.user
        ).order_by("-created_at")
