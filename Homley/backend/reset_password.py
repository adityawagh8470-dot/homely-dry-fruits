import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

try:
    user = User.objects.get(username="admin")
    user.set_password("admin123")
    user.is_active = True
    user.save()
    print("Successfully reset password for user 'admin' to 'admin123'")
    print(f"User 'admin' is_active: {user.is_active}")
except User.DoesNotExist:
    print("User 'admin' does not exist. Creating it...")
    User.objects.create_user(username="admin", email="admin@example.com", password="admin123")
    print("Created user 'admin' with password 'admin123'")
