# Generated by Django 5.0 on 2024-01-08 20:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_comment_options_alter_post_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='blog/'),
        ),
    ]
