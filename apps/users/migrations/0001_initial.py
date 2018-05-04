# Generated by Django 2.0.5 on 2018-05-03 21:57

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('last_login', models.DateTimeField(
                    blank=True, null=True, verbose_name='last login')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False,
                                          primary_key=True, serialize=False, unique=True, verbose_name='pk')),
                ('email', models.EmailField(
                    max_length=254, unique=True, verbose_name='이메일')),
                ('username', models.CharField(max_length=20, verbose_name='닉네임')),
                ('password', models.CharField(max_length=100, verbose_name='비밀번호')),
                ('date_joined', models.DateTimeField(
                    auto_now_add=True, verbose_name='가입일')),
                ('is_active', models.BooleanField(
                    default=True, verbose_name='휴면 계정 여부')),
                ('is_admin', models.BooleanField(
                    default=False, verbose_name='관리자 계정 여부')),
            ],
            options={
                'verbose_name': '인내의 숲 유저',
                'verbose_name_plural': '인내의 숲 유저들',
                'db_table': 'patienceforest-users',
            },
        ),
    ]
