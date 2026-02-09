from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ["id", "name"]


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)

    # ✅ Return Cloudinary Image URL
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "description",
            "price",
            "stock",
            "image_url",
            "is_active",
            "created_at",
        ]

    def get_image_url(self, obj):
        """
        Converts CloudinaryField to real URL
        """
        try:
            if obj.image:
                return obj.image.url
        except Exception:
            return None
        return None


# ✅ For Admin/Product Create/Update (when adding product)
class ProductCreateUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            "id",
            "category",
            "name",
            "description",
            "price",
            "stock",
            "image",
            "is_active",
        ]
