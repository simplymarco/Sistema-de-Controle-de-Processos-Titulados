# Generated by Django 3.0 on 2020-11-11 18:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0015_auto_20201111_1429'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='interessado',
            field=models.ManyToManyField(to='accounts.Interessado'),
        ),
    ]