# Generated by Django 4.2.2 on 2023-07-20 23:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0007_remove_user_bio_remove_user_birth_date_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='title',
        ),
    ]
