# Generated by Django 3.1.6 on 2021-04-01 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learn', '0006_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('password', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
    ]