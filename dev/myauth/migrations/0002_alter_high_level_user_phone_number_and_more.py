# Generated by Django 4.1.6 on 2023-02-10 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myauth', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='high_level_user',
            name='phone_number',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='low_level_user',
            name='phone_number',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='mid_level_user',
            name='phone_number',
            field=models.CharField(max_length=250),
        ),
    ]