# Generated by Django 4.1.3 on 2023-07-29 23:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(upload_to='blog/images')),
                ('date', models.DateField()),
            ],
        ),
    ]
