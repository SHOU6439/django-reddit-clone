from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None):
        if not username:
            raise ValueError('Users must have a username')
        elif not email:
            raise ValueError('Users must have an email address')
        elif not password:
            raise not ValueError('Users must have a password')

        user = self.model(
            username = username,
            email = self.normalize_email(email)
        )
        user.set_password(password)
        user.save(using=self._db)

        return user

class User(AbstractBaseUser, PermissionsMixin):
    username_validator = UnicodeUsernameValidator()

    username = models.CharField(
        max_length=20,
        validators=[username_validator],
        unique=True
    )

    about = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )


    email = models.EmailField(blank=True)


    photo = models.ImageField(verbose_name='写真', blank=True, null=True, upload_to='images/')
    thumbnail = ImageSpecField(source='photo', processors=[ResizeToFill(80, 80)], format='JPEG', options={'quality': 60})

    header_photo = models.ImageField(verbose_name='ヘッダー写真', blank=True, null=True, upload_to='images/')
    header = ImageSpecField(source='header_photo', processors=[ResizeToFill(312, 94)], format='JPEG', options={'quality': 60})



    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email']

    class Meta:
        db_table = 'users'