# Generated by Django 4.2.3 on 2023-08-04 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scripts',
            name='exch_seg',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='expiry',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='instrumenttype',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='lotsize',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='strike',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='symbol',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='tick_size',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='scripts',
            name='token',
            field=models.CharField(max_length=100),
        ),
    ]
