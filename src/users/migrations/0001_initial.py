# Generated by Django 3.1.6 on 2021-04-10 06:15

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdgeUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Full name of user')),
                ('picture', models.ImageField(blank=True, null=True, upload_to='profile_pics/', verbose_name='Profile picture')),
                ('slug', models.UUIDField(blank=True, default=uuid.uuid4, editable=False)),
            ],
            options={
                'verbose_name': 'user',
            },
        ),
    ]