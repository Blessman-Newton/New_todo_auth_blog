# Generated by Django 4.0.6 on 2022-10-03 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_email_reister_emails'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Reister',
            new_name='Register',
        ),
    ]
