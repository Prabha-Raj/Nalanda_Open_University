# Generated by Django 4.2.4 on 2023-09-09 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nouapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Email',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emailaddress', models.CharField(max_length=50)),
            ],
        ),
    ]
