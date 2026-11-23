from rest_framework.views import APIView
from rest_framework.response import Response
from products.models import Product


class ChatbotAPIView(APIView):

    def post(self, request):

        message = request.data.get("message", "").lower().strip()

        # Greeting messages
        greetings = ["hi", "hello", "hey", "hii"]

        if message in greetings:
            return Response({
                "reply": "Hi 👋 I am Homely Assistant! Ask me about any dry fruits, nuts, seeds or makhana."
            })

        # Help command
        if "help" in message:
            return Response({
                "reply": "You can ask me about products like Almonds, Cashews, Raisins, Pistachios, Makhana, Chia Seeds and many more."
            })

        # Cheap products recommendation
        if "cheap" in message or "low price" in message:

            products = Product.objects.order_by("price")[:3]

            reply = "Here are some affordable products:\n"

            for p in products:
                reply += f"{p.name} - ₹{p.price}\n"

            return Response({"reply": reply})

        # Show product list
        if "products" in message or "show products" in message:

            products = Product.objects.all()[:10]

            reply = "We have these products:\n"

            for p in products:
                reply += f"{p.name}\n"

            return Response({"reply": reply})

        # Product search
        products = Product.objects.all()

        for product in products:

            name = product.name.lower()

            if name in message:

                reply = f"""
{product.name}

Price: ₹{product.price}

Description: {product.description}
"""

                return Response({
                    "reply": reply
                })

        # Fallback search
        product = Product.objects.filter(name__icontains=message).first()

        if product:

            reply = f"""
{product.name}

Price: ₹{product.price}

Description: {product.description}
"""

            return Response({
                "reply": reply
            })

        return Response({
            "reply": "Sorry, I could not find that product."
        })