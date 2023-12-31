# Generated by Django 4.1.7 on 2023-06-01 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Budget_table',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('budget_type', models.CharField(choices=[('add', '+'), ('sub', '-')], max_length=50)),
                ('income', models.IntegerField()),
                ('expense', models.IntegerField()),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
