# Generated by Django 4.2.6 on 2023-12-19 14:56

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('income', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Expense',
            new_name='Income',
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
    ]
