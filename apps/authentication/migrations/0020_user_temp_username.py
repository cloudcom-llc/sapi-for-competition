# Generated by Django 5.2 on 2025-06-25 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0019_alter_user_phone_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='temp_username',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='temp username'),
        ),
    ]
