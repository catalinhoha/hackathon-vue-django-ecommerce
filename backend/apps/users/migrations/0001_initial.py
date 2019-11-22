# Generated by Django 2.2.7 on 2019-11-22 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(choices=[('seller', 'Seller'), ('buyer', 'Buyer')], max_length=10)),
                ('full_name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=11)),
                ('address', models.CharField(max_length=255)),
                ('buyer_type', models.CharField(choices=[('private', 'Private'), ('company', 'Company')], max_length=10)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
