from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.contrib.auth.base_user import BaseUserManager

    
class CustomUserManager(BaseUserManager):
    
    def create_user(self, email, username ,password, **extra_fields):
        if not email:
            return ValueError("User must have an email")

        if not username:
            return ValueError("User must have a name")
        
        email = self.normalize_email(email)
        user = self.model(email=email, 
                        username=username, 
                        **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, username, password, **extra_fields):

        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        if extra_fields.get('is_staff') is not True:
            raise ValueError(_('Superuser must have is_staff=True.'))
        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        email = self.normalize_email(email)
        return self.create_user(email, username, password, **extra_fields)

class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=70, unique=True)
    username = models.CharField(verbose_name="username", max_length=50, unique=True)
    picture = models.ImageField(blank=True, null=True)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = CustomUserManager()

    def __str__(self):
        return self.username

    # AFTER ADDING PermissionsMixin cod bellow is unnecessary
    # def has_perm(self, perm, obj=None):
    #     return self.is_superuser

    # def has_module_perms(self, app_label):
    #     return self.is_superuser
