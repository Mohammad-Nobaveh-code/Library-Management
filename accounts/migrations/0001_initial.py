# Generated by Django 4.1 on 2022-08-13 18:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=30)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'female')], max_length=1)),
                ('address', models.TextField()),
                ('national_code', models.CharField(max_length=12)),
            ],
        ),
    ]
