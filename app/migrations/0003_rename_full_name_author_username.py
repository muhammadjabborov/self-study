# Generated by Django 4.1.2 on 2022-10-19 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_comment_table'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='full_name',
            new_name='username',
        ),
    ]