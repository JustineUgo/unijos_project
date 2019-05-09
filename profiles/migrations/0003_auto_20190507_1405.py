# Generated by Django 2.0.6 on 2019-05-07 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20190507_1403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('100lvl', '100 LEVEL'), ('200lvl', '200 LEVEL'), ('300lvl', '300 LEVEL'), ('400lvl', '400 LEVEL'), ('500lvl', '500 LEVEL')], default='100lvl', max_length=40),
        ),
    ]