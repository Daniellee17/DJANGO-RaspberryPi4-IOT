# Generated by Django 2.1.5 on 2019-04-01 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='sensors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('temperature', models.FloatField(max_length=250)),
                ('moisture', models.FloatField(max_length=250)),
                ('humidity', models.FloatField(max_length=250)),
                ('camera', models.ImageField(blank=True, default='default.png', upload_to='')),
            ],
        ),
    ]