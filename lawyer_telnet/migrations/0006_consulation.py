# Generated by Django 3.1.2 on 2020-11-21 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lawyer_telnet', '0005_mediacomment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Consulation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True)),
                ('email', models.EmailField(blank=True, default='', max_length=70, null=True)),
                ('phone', models.CharField(blank=True, max_length=70, null=True)),
                ('address', models.CharField(blank=True, max_length=200, null=True)),
                ('message', models.CharField(blank=True, max_length=10000, null=True)),
            ],
        ),
    ]
