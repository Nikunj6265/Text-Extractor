# Import necessary modules
from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager

# Custom user model
class User(AbstractBaseUser):
    # User fields
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    # Manager instance
    objects = UserManager()

    # Field for user identification
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    # Methods for permissions and user details
    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

# Paragraph model
class Paragraph(models.Model):
    text = models.TextField()

# Word model
class Word(models.Model):
    word = models.CharField(max_length=100)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)