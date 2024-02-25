from django.db import models
from django.utils import timezone
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from authorization.managers import UserManager

class User(AbstractBaseUser,PermissionsMixin):
    SUPERADMIN, COURIER, BASIC = range(1, 4)

    objects = UserManager()

    ROLE_GROUP = {
        SUPERADMIN: 1,
        COURIER: 2,
        BASIC: 3,
    }

    ROLE_TYPES = (
        (SUPERADMIN, 'Суперадмин'),
        (COURIER, 'Курьер'),
        (BASIC, 'Покупатель'),
    )


    IS_ACTIVE = (
        (True, 'Не заблокирован'),
        (False, 'Заблокирован'),
    )

    id = models.AutoField(primary_key=True)
    username = models.CharField(verbose_name='Номер телефона (логин)', max_length=50, default='', unique=True)
    role = models.IntegerField(verbose_name='Роль', default=BASIC, choices=ROLE_TYPES)
    first_name = models.CharField(verbose_name="ФИО",max_length=100, default='', blank=True,null=True)
    email = models.EmailField(verbose_name="Email",max_length=100,default='',null=True,blank=True)
    date_joined=models.DateTimeField(verbose_name="Дата присоединения",blank=True,null=True,default=timezone.now)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(
        default=True,
        choices=IS_ACTIVE,
        verbose_name='Статус доступа',
    )
    blocked=models.BooleanField(verbose_name="Пользователь заблокирован",default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return str(self.username) + " - " + str(self.first_name)
    
    def save(self, *args, **kwargs):
        # Если пароль не хэширован, то хэшируем его перед сохранением
        if not self.password.startswith('pbkdf2_sha256'):
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
