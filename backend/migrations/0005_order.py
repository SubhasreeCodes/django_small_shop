# Generated by Django 5.1.5 on 2025-01-28 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('order_number', models.CharField(blank=True, max_length=255, null=True)),
                ('order_date', models.DateTimeField(auto_now_add=True)),
                ('total_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]
