# Generated by Django 4.0.5 on 2022-07-14 14:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0011_alter_product_prodtype_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='product',
            name='Cat_Name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='base.category', verbose_name='Category'),
        ),
    ]
