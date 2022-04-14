# Generated by Django 3.2.11 on 2022-04-04 16:07

from django.db import migrations, models
import django_countries.fields
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('pkid', models.BigAutoField(editable=False, primary_key=True, serialize=False)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(default='+250784123456', max_length=30, region=None, verbose_name='phone number')),
                ('max_length', models.TextField(default='say something about yourself', verbose_name='about me')),
                ('gender', models.CharField(choices=[('male', 'male'), ('female', 'female'), ('other', 'other')], default='other', max_length=20, verbose_name='gender')),
                ('country', django_countries.fields.CountryField(default='US', max_length=2, verbose_name='country')),
                ('city', django_countries.fields.CountryField(default='New York', max_length=180, verbose_name='city')),
                ('profile_photo', models.ImageField(default='/profile_default.png', upload_to='', verbose_name='profile photo')),
                ('twitter_handle', models.CharField(blank=True, max_length=20, verbose_name='twitter_handle')),
                ('follows', models.ManyToManyField(blank=True, related_name='followed_by', to='profiles.Profile')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
