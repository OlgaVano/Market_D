from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, full_name, password, is_manager):
        if not email:
            raise ValueError('Email is required!')
        if not full_name:
            raise ValueError('full name is required!')

        user = self.model(email=self.normalize_email(email), full_name=full_name, is_manager=is_manager)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, email, full_name, password):
        user = self.create_user(email, full_name, password)
        user.is_admin = True
        user.save(using=self.db)
        return user


