# Generated by Django 4.1.7 on 2023-04-09 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_app_question_data_of_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='url',
            field=models.CharField(default='', max_length=10000),
            preserve_default=False,
        ),
    ]
