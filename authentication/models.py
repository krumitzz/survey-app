from django.db import models
from django.contrib.auth.models import (
    BaseUserManager,
    AbstractBaseUser,
    Group
)

class SurveyAppUserManager(BaseUserManager):

    def create_user(self, email, password=None):

        """
        Raises:
            ValueError: [description]
        Returns:
            user [object]: [description]
        """

        if not email:
            raise ValueError('user must enter a valid email address')

        user = self.model(
            email=self.normalize_email(email)
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        """
        Args:
            email ([type]): [description]
            password ([type], optional): [description]. Defaults to None.
        """

        user = self.create_user(
            email=email,
            password=password
        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    email = models.EmailField('Email Address', unique=True)
    username = models.CharField('Username', max_length=60, blank=True)

    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    groups = models.ManyToManyField(Group)

    objects = SurveyAppUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        """[summary]

        Args:
            perm ([type]): [description]
            obj ([type], optional): [description]. Defaults to None.
        """
        return True

    def has_module_perms(self, app_label):
        """[summary]

        Args:
            app_label ([type]): [description]
        """
        return True

    @property
    def is_staff(self):
        """

        """
        return self.is_admin