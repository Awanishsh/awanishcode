# Generated by Django 4.0.3 on 2022-04-11 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_applylist'),
    ]

    operations = [
        migrations.AddField(
            model_name='usermaster',
            name='is_created',
            field=models.DateTimeField(auto_now_add=True, default=0),
            preserve_default=False,
        ),
    ]
