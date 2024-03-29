# Generated by Django 2.2.2 on 2019-09-02 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message_user', models.CharField(max_length=20)),
                ('message_text', models.CharField(max_length=20)),
                ('message_contect', models.CharField(max_length=100)),
                ('message_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('creation_time', models.DateTimeField()),
            ],
        ),
    ]
