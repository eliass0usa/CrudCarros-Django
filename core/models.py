import re
from django.db import models
from django.utils import timezone
from django.core import validators
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    cpf = models.CharField(max_length=11, null=False, default="")
    nome = models.CharField(max_length=50, null=False, default="")
    sobrenome = models.CharField(max_length=100, null=False, default="") 
    nascimento = models.DateField()

    def __str__(self):
        return self.nome

class Carro(models.Model):
    nome = models.CharField(max_length=50, null=False, default="")
    marca = models.CharField(max_length=100, null=False, default="")
    placa = models.CharField(max_length=8, null=False, default="")
    cor = models.CharField(max_length=20, null=False, default="")
    ano = models.IntegerField(null=False)
    cliente = models.ForeignKey(to='core.Cliente', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.nome

class UserManager(BaseUserManager):
    def _create_user(self, username, email, password, is_staff, is_superuser):
        now = timezone.now()
        if not username:
            raise ValueError(_('Informe o nome de usuário'))
        email = self.normalize_email(email)
        user = self.model(
            username=username, email=email, is_staff=is_staff, is_active=True,
            is_superuser=is_superuser, last_login=now, date_joined=now
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None):
        return self._create_user(username, email, password, False, False)

    def create_superuser(self, username, email, password):
        user = self._create_user(username, email, password, True, True)
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        _('username'), max_length=15, unique=True,
        help_text=_('Required. 15 characters or fewer. Letters, numbers and @/./+/-/_ characters'),
        validators=[validators.RegexValidator(
            re.compile(r'^[\w.@+-]+$'),
            _('Insira um nome de usuário válido.'),
            _('inválido')
        )]
    )
    first_name = models.CharField(_('Primeiro nome'), max_length=30)
    last_name = models.CharField(_('Último nome'), max_length=30)
    email = models.EmailField(_('endereço de email'), max_length=255, unique=True)
    is_staff = models.BooleanField(
        _('status de administrador'), default=False,
        help_text=_('Designates whether the user can log into this admin site.')
    )
    is_active = models.BooleanField(
        _('active'), default=True,
        help_text=_('Designates whether this user should be treated as active. Unselect this instead of deleting accounts.')
    )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)
    is_trusty = models.BooleanField(
        _('trusty'), default=False,
        help_text=_('Designates whether this user has confirmed his account.')
    )

    groups = models.ManyToManyField(
        'auth.Group',
        related_name='core_user_set',
        blank=True,
        help_text=_('The groups this user belongs to. A user will get all permissions granted to each of their groups.'),
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
