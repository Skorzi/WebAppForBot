# Generated by Django 4.1.3 on 2022-11-22 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexApp', '0002_disliketable_grademodel_liketable_usertelegram_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertelegram',
            name='id_tg',
            field=models.CharField(default=None, max_length=64, unique=True),
        ),
    ]