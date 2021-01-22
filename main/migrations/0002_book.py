# Generated by Django 2.2 on 2021-01-21 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=50)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('genre', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('year', models.IntegerField(max_length=4)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
