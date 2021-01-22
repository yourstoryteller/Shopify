# Generated by Django 3.1.5 on 2021-01-19 12:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_discount'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discount',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', unique=True),
        ),
    ]
