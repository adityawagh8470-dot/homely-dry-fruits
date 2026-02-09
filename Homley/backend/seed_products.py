from products.models import Product, Category

# Ensure Category exists
category, _ = Category.objects.get_or_create(name="Dry Fruits")

products = [
    {"name": "Almonds", "price": 400, "image": "./assets/images/Almonds.jpg"},
    {"name": "Cashews", "price": 820, "image": "./assets/images/Cashews.jpg"},
    {"name": "Raisins", "price": 420, "image": "./assets/images/Raisins.jpg"},
    {"name": "Pistachios", "price": 980, "image": "./assets/images/Pistachios.jpg"},
    {"name": "Walnuts", "price": 680, "image": "./assets/images/Walnuts.jpg"},
    {"name": "Dried Figs", "price": 900, "image": "./assets/images/Driedfigs.jpg"},
    {"name": "Dates", "price": 350, "image": "./assets/images/Dates.jpg"},
    {"name": "Apricots", "price": 850, "image": "./assets/images/Apricots.jpg"},
    {"name": "Black Raisins", "price": 480, "image": "./assets/images/Black Raisins.jpg"},
    {"name": "Cranberries", "price": 620, "image": "./assets/images/Cranberries.jpg"},
    {"name": "Peanuts", "price": 220, "image": "./assets/images/Peanuts.jpg"},
    {"name": "Hazelnuts", "price": 1100, "image": "./assets/images/Hazelnuts.jpg"},
    {"name": "Macadamia Nuts", "price": 1400, "image": "./assets/images/MacadamiaNuts.jpg"},
    {"name": "Pine Nuts", "price": 1600, "image": "./assets/images/PineNuts.jpg"},
    {"name": "Chia Seeds", "price": 320, "image": "./assets/images/ChiaSeeds.jpg"},
    {"name": "Flax Seeds", "price": 280, "image": "./assets/images/FlaxSeeds.jpg"},
    {"name": "Pumpkin Seeds", "price": 420, "image": "./assets/images/PumpkinSeeds.jpg"},
    {"name": "Sunflower Seeds", "price": 300, "image": "./assets/images/Sunflowerseeds.jpg"},
    {"name": "Makhana", "price": 520, "image": "./assets/images/Makhana.jpg"},
    {"name": "Roasted Foxnuts", "price": 580, "image": "./assets/images/RoastedFoxnuts.jpg"},
]

for p in products:
    obj, created = Product.objects.get_or_create(
        name=p["name"],
        defaults={
            "price": p["price"],
            "image": p["image"],
            "category": category,
            "description": "Premium quality " + p["name"]
        }
    )
    if created:
        print(f"Created {p['name']}")
    else:
        print(f"Exists {p['name']}")
