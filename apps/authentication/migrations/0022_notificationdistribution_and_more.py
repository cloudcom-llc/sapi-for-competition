# Generated by Django 5.2 on 2025-06-27 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0021_usersubscription_created_at_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificationDistribution',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('is_draft', models.BooleanField(default=False)),
                ('title_uz', models.CharField(blank=True, max_length=155, null=True)),
                ('title_ru', models.CharField(blank=True, max_length=155, null=True)),
                ('text_uz', models.TextField(blank=True, null=True)),
                ('text_ru', models.TextField(blank=True, null=True)),
                ('sending_date', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(choices=[('waiting', 'Ожидается')], default='waiting', max_length=55)),
                ('user_type', models.CharField(choices=[('all', 'Все пользователи'), ('creators', 'Креаторы'), ('users', 'Обычные пользователи')], default='all', max_length=55)),
                ('type', models.CharField(choices=[('push_notification', 'Push-уведомление')], default='push_notification', max_length=55)),
            ],
            options={
                'db_table': 'notification_distribution',
            },
        ),
        migrations.AlterField(
            model_name='userpermissions',
            name='permission',
            field=models.CharField(choices=[('VIEW_STATISTICS', 'Просмотр статистики'), ('MODIFY_STATISTICS', 'Редактирование статистики'), ('VIEW_NOTIFICATIONS', 'Просмотр рассылок уведомлений'), ('MODIFY_NOTIFICATIONS', 'Редактирование рассылок уведомлений'), ('VIEW_REPORTS', 'Просмотр жалоб'), ('MODIFY_REPORTS', 'Редактирование жалоб'), ('VIEW_CREATORS', 'Просмотр креаторов'), ('MODIFY_CREATORS', 'Редактирование креаторов'), ('VIEW_CHATS', 'Просмотр чата поддержки'), ('MODIFY_CHATS', 'Редактирование чата поддержки'), ('VIEW_ADMINS', 'Просмотр администраторов'), ('MODIFY_ADMINS', 'Редактирование администраторов')], max_length=55),
        ),
    ]
