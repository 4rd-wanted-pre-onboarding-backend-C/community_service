# Generated by Django 4.1 on 2022-09-05 02:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_phone'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='teamgroup',
        ),
        migrations.AlterField(
            model_name='user',
            name='age',
            field=models.PositiveIntegerField(verbose_name='나이'),
        ),
        migrations.DeleteModel(
            name='TeamGroup',
        ),
    ]