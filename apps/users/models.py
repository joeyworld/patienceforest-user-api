import uuid
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class UserManager(BaseUserManager):
    def _create_user(self, email, password=None, **kwargs):
        if not email:
            raise ValueError('이메일은 필수 항목입니다.')
        if 'username' not in kwargs:
            raise ValueError('닉네임은 필수 항목입니다.')

        new_user = self.model(email=self.normalize_email(email), **kwargs)
        new_user.set_password(password)
        new_user.save(using=self.db)
        return new_user

    def create_user(self, email, password, **kwargs):
        kwargs.setdefault('is_admin', False)
        return self._create_user(email, password, **kwargs)

    def create_superuser(self, email, password, **kwargs):
        kwargs.setdefault('is_admin', True)
        return self._create_user(email, password, **kwargs)


class User(AbstractBaseUser):
    uuid = models.UUIDField(
        primary_key=True,
        unique=True,
        editable=False,
        default=uuid.uuid4,
        verbose_name='pk'
    )
    email = models.EmailField(unique=True, verbose_name='이메일')
    username = models.CharField(max_length=20, verbose_name='닉네임')
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name='가입일')
    is_active = models.BooleanField(default=True, verbose_name='활성화 된 계정')
    is_admin = models.BooleanField(default=False, verbose_name='관리자 계정')

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    @property
    def is_staff(self):
        return self.is_admin

    def has_perm(self, perm, obj=None):
        # TODO implementation
        return True

    def has_module_perms(self, app_label):
        # TODO implementation
        return True

    def __str__(self):
        return 'User : email={}, username={}'.format(self.email, self.username)

    class Meta:
        db_table = 'patienceforest-users'
        verbose_name = '인내의 숲 유저'
        verbose_name_plural = '인내의 숲 유저들'
