# Generated by Django 4.2.6 on 2024-03-20 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='products',
            old_name='descr',
            new_name='name',
        ),
    ]