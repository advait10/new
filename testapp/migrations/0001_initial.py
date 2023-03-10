# Generated by Django 4.1.1 on 2023-02-23 14:09

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=30)),
                ('email_id', models.CharField(max_length=30)),
                ('company_code', models.CharField(max_length=50, validators=[django.core.validators.RegexValidator('^[0-9a-zA-Z]*$', 'Only alphanumeric characters are allowed.')])),
                ('strength', models.IntegerField()),
                ('website', models.URLField()),
                ('created_time', models.TimeField(auto_now=True)),
            ],
            options={
                'db_table': 'emp',
            },
        ),
    ]
