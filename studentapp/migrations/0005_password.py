# Generated by Django 4.2.4 on 2023-09-15 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0004_delete_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Password',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('oldpassword', models.CharField(max_length=30)),
                ('newpassword', models.CharField(max_length=30)),
                ('confirmpassword', models.CharField(max_length=30)),
            ],
        ),
    ]
