from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# Create your models here.


class AccountManager(BaseUserManager):
    # this one is done using command line? all for django items
    def create_user(self, email, name, role, department, password=None):
        if not email:
            raise ValueError('User must have a valid email')

        user = self.model(
            # this will make it all to small letters
            email=self.normalize_email(email),
        )
        user.name = name
        user.role = role
        user.department = department
        # this uses encryption process (auto)
        user.set_password(password)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, password):
        # what is returned is at the start
        user = self.create_user(
            email=email,
            password=password
        )
        # superuser is true for all
        user.is_staff = True
        user.is_superuser = True
        user.is_admin = True
        user.save(using=self._db)

        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name='email', max_length=60, unique=True)
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=250)
    role = models.ForeignKey('restful_apis.Role', on_delete=models.DO_NOTHING, null=True)
    department = models.ForeignKey('restful_apis.Department', on_delete=models.DO_NOTHING, null=True)
    is_superuser = models.BooleanField(default=False)

    objects = AccountManager()

    USERNAME_FIELD = 'email'
    # REQUIRED_FIELDS = ['email']

    # forcing it to return only the surname and name
    def __str__(self):
        return f'{self.name}'

    # has parameters. allows certain part of the user interface to be locked down. only for admin
    def has_perm(self, perm, obj=None):
        return self.is_admin

    # creating different webpages for different things??
    def has_module_perms(self, app_label):
        return True