# Generated by Django 3.0.8 on 2020-07-29 16:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Device', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='devicecategory',
            options={'verbose_name': '设备类别'},
        ),
        migrations.AlterModelOptions(
            name='vender',
            options={'verbose_name': '厂家', 'verbose_name_plural': '厂家'},
        ),
    ]