# Generated by Django 5.0.3 on 2024-03-18 01:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='warehouses',
            name='material_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.material', verbose_name='homashiyo id'),
        ),
    ]
