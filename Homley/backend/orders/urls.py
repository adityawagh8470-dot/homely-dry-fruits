from django.urls import path
from .views import PlaceOrderAPIView, UserOrdersAPIView

urlpatterns = [
    path("place/", PlaceOrderAPIView.as_view()),
    path("my-orders/", UserOrdersAPIView.as_view()),
]
