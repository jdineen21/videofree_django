# Generated by Django 2.2.7 on 2019-12-04 08:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('footage', '0004_auto_20191204_0813'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footage',
            name='uuid',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]