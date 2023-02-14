# Generated by Django 4.1.6 on 2023-02-03 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=30)),
                ('Phone', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=30)),
                ('website', models.URLField()),
                ('description', models.TextField(max_length=500)),
            ],
        ),
    ]
