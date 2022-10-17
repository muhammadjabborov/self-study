# Generated by Django 4.1.2 on 2022-10-17 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now=True)),
                ('updated_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(upload_to='post-images/')),
                ('description', models.TextField()),
            ],
            options={
                'db_table': 'posts',
            },
        ),
    ]