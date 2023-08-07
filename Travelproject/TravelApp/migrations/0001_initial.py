# Generated by Django 4.1.3 on 2023-07-14 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('place', models.CharField(max_length=250)),
                ('img', models.ImageField(upload_to='Pics')),
                ('description', models.TextField()),
            ],
        ),
    ]