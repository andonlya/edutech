# Generated by Django 4.0 on 2022-06-03 07:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('edutech_app', '0012_alter_currentcourse_c_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='currentcourse',
            old_name='c_username',
            new_name='c_email',
        ),
    ]
