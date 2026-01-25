from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, cnic, password=None, **extra_fields):
        if not cnic:
            raise ValueError("CNIC is required")
        user = self.model(cnic=cnic, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, cnic, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(cnic, password, **extra_fields)
