# Generated by Django 2.2 on 2020-03-14 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjass_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(null=True),
        ),
    ]
