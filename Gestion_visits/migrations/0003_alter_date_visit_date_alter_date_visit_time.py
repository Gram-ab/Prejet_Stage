# Generated by Django 4.0.3 on 2022-04-13 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Gestion_visits', '0002_remove_date_time_date_visit_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='visit_date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='date',
            name='visit_time',
            field=models.TimeField(null=True),
        ),
    ]