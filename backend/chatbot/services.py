from products.models import Product

def get_product_info(query):

    products = Product.objects.filter(name__icontains=query)

    if products.exists():
        product = products.first()

        return f"""
Product: {product.name}
Price: ₹{product.price}
Description: {product.description}
"""

    return "Sorry, I could not find that product."