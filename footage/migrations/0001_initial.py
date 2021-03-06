# Generated by Django 2.2.7 on 2019-11-25 01:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Footage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('upload_datetime', models.DateTimeField()),
                ('tags', models.CharField(choices=[('ACT', 'Action Stock'), ('DRN', 'Drone Stock'), ('LND', 'Landscapes Stock'), ('OTH', 'Other')], default='OTH', max_length=3)),
                ('description', models.TextField()),
            ],
        ),
    ]
