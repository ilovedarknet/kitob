# Generated by Django 4.0.1 on 2022-01-14 10:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion
import user.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('address', models.TextField(verbose_name='address')),
                ('phone', models.CharField(max_length=14, validators=[user.validators.PhoneValidator()], verbose_name='phone')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
            ],
            options={
                'verbose_name': 'about-us',
                'verbose_name_plural': 'about-us',
            },
        ),
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('description', models.TextField(verbose_name='description')),
                ('image', models.ImageField(upload_to='AboutUs/', verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='title')),
                ('isbn', models.IntegerField(default=0, verbose_name='isbn')),
                ('author', models.CharField(max_length=100, verbose_name='author')),
                ('publishing', models.CharField(max_length=150, verbose_name='publishing')),
                ('description', ckeditor.fields.RichTextField(verbose_name='description')),
                ('count_sell', models.IntegerField(verbose_name='count_sell')),
                ('price', models.BigIntegerField(default=0, verbose_name='price')),
                ('seen', models.IntegerField(default=0, verbose_name='seen')),
                ('image', models.ImageField(upload_to='book-image/', verbose_name='image')),
                ('rating', models.IntegerField(default=0, verbose_name='rating')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
            options={
                'verbose_name': 'book',
                'verbose_name_plural': 'books',
            },
        ),
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.TextField(verbose_name='address')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('booking', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='api.booking', verbose_name='booking')),
            ],
        ),
    ]
