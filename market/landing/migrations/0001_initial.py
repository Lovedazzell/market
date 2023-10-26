# Generated by Django 3.2.18 on 2023-07-24 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=26)),
                ('number', models.BigIntegerField()),
                ('alternative_number', models.BigIntegerField(blank=True, null=True)),
                ('address1', models.CharField(max_length=300)),
                ('address2', models.CharField(max_length=300)),
                ('city', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('zip', models.CharField(max_length=300)),
                ('payment_mode', models.CharField(blank=True, max_length=300, null=True)),
                ('payment_status', models.BooleanField(default=False)),
                ('order_status_pending', models.BooleanField(default=True)),
                ('order_status_deliverd', models.BooleanField(default=False)),
                ('order_status_failed', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]