import re
from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, null=False, default="", unique=True)
    nome = models.CharField(max_length=50, null=False, default="")
    sobrenome = models.CharField(max_length=100, null=False, default="")
    nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Carro(models.Model):
    nome = models.CharField(max_length=50, null=False, default="")
    marca = models.CharField(max_length=100, null=False, default="")
    placa = models.CharField(max_length=8, null=False, default="", unique=True)
    cor = models.CharField(max_length=20, null=False, default="")
    ano = models.IntegerField(null=False)
    cliente = models.ForeignKey(to='Cliente', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_superuser=True):
        if not username:
            raise ValueError(_('The Username field must be set'))
        if not email:
            raise ValueError(_('The Email field must be set'))
        
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            password=password,
            is_superuser=is_superuser,
            is_active=True
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, password):
        return self._create_user(username, email, password, is_staff=True, is_superuser=True)

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), max_length=15, unique=True,
        help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
        validators=[validators.RegexValidator(
            re.compile(r'^[\w.@+-]+$'),
            _('Enter a valid username.'),
            _('invalid')
        )]
    )
    first_name = models.CharField(_('first name'), max_length=30)
    last_name = models.CharField(_('last name'), max_length=30)
    email = models.EmailField(_('email address'), max_length=255, unique=True)  
    
    is_staff = models.BooleanField(
        _('staff status'), default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as active.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(
        _('trusty'), default=False,
        help_text=_('Designates whether this user has confirmed their account.')
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',
        blank=True,
        help_text=_('The groups this user belongs to.'),
        verbose_name=_('groups'),
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='core_user_permissions',
        blank=True,
        help_text=_('Specific permissions for this user.'),
        verbose_name=_('user permissions'),
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name']

    objects = UserManager()

    def __str__(self):
        return self.username