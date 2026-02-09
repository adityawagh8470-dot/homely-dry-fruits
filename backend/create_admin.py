from django.contrib.auth import get_user_model
try:
    User = get_user_model()
    if not User.objects.filter(username='admin').exists():
        User.objects.create_superuser('admin', 'admin@example.com', 'admin')
        print("Superuser 'admin' created.")
    else:
        print("Superuser 'admin' already exists.")
except Exception as e:
    print(f"Error creating user: {e}")
