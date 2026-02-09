import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "backend.settings")
django.setup()

from django.contrib.auth import get_user_model
User = get_user_model()

count = User.objects.count()
print(f"User count: {count}")

if count == 0:
    print("Creating test user 'admin' with password 'password'...")
    User.objects.create_user(username="admin", email="admin@example.com", password="password")
    print("Test user created.")
else:
    print("Users exist.")
    for u in User.objects.all():
        print(f" - {u.username} ({u.email}) [Name: {u.first_name} {u.last_name}]")
