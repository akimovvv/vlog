# Generated by Django 3.2.8 on 2022-01-03 15:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0003_sliderimage'),
    ]

    operations = [
        migrations.CreateModel(
            name='AboutMe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
            ],
        ),
    ]