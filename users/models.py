from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.contrib.auth.validators import UnicodeUsernameValidator
from imagekit.models import ImageSpecField, ProcessedImageField
from imagekit.processors import ResizeToFill

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

    is_staff = models.BooleanField(
        ('staff status'),
        default=False,
        help_text=('Designates whether the user can log into this admin site.'),
    )

    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username'
    REQUIRED_FIELD = ['email']

    class Meta:
        db_table = 'users'