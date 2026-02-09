from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

def home(request):
    return JsonResponse({"message": "Welcome to Homley API", "status": "Running"})

urlpatterns = [
    path("", home),
    path("admin/", admin.site.urls),

    # AUTH
    path("api/auth/", include("users.urls")),
    
    path("api/auth/", include("rest_framework.urls")),

    # PRODUCTS (Public)
    path("api/", include("products.urls")),

    # ORDERS (User)
    path("api/orders/", include("orders.urls")),

    # 🔥 ADMIN PANEL ROUTES
    path("api/admin/", include("admin_api.urls")),
]



