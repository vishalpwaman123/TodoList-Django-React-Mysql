# Generated by Django 3.2 on 2021-04-19 12:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('System_Authentication', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccoutdetail',
            old_name='user_id',
            new_name='id',
        ),
    ]