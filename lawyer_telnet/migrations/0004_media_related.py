# Generated by Django 3.1.2 on 2020-11-21 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer_telnet', '0003_media'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='related',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
