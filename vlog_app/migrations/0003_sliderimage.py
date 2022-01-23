# Generated by Django 3.2.8 on 2022-01-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vlog_app', '0002_social_medial'),
    ]

    operations = [
        migrations.CreateModel(
            name='SliderImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='media/%Y/%m/%d', verbose_name='image')),
                ('video', models.FileField(upload_to='media/%Y/%m/%d', verbose_name='video')),
            ],
        ),
    ]
