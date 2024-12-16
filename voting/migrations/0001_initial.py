# Generated by Django 5.0 on 2024-12-09 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('real_name', models.CharField(blank=True, max_length=100, null=True)),
                ('photo_url', models.URLField(blank=True, null=True)),
                ('votes', models.IntegerField(default=0)),
            ],
        ),
    ]
