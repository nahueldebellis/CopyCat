# Generated by Django 2.2.1 on 2019-06-02 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('welcome', '0002_users_born_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(default='nan', max_length=50),
        ),
    ]
