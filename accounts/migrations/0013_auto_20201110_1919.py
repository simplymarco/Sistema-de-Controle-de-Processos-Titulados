# Generated by Django 3.0 on 2020-11-10 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0012_auto_20201110_1908'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='processo',
            name='interessado',
        ),
        migrations.AddField(
            model_name='processo',
            name='interessado',
            field=models.ManyToManyField(to='accounts.Interessado'),
        ),
    ]
