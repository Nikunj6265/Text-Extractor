from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import UserManager
# Create your models here.
class User(AbstractBaseUser):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True)
    name = models.CharField(max_length=100)
    dob = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ["name"]

    def __str__(self):
        return self.email
    
    def get_full_name(self):
        return self.name
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
    
class Paragraph(models.Model):
    text = models.TextField()

class Word(models.Model):
    word = models.CharField(max_length=100)
    paragraph = models.ForeignKey(Paragraph, on_delete=models.CASCADE)