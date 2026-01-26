#!/usr/bin/env bash
pip install -r requirements.txt

python manage.py migrate
python manage.py collectstatic --noinput

# AUTO CREATE SUPERUSER (ONLY IF NOT EXISTS)
python manage.py shell <<EOF
from django.contrib.auth import get_user_model
User = get_user_model()

CNIC = "3540487138783"
PASSWORD = "Admin@123"
FULL_NAME = "Admin User"
CONSTITUENCY = "ADMIN"

if not User.objects.filter(cnic=CNIC).exists():
    User.objects.create_superuser(
        cnic=CNIC,
        password=PASSWORD,
        full_name=FULL_NAME,
        constituency=CONSTITUENCY
    )
    print("Superuser created")
else:
    print("Superuser already exists")
EOF
