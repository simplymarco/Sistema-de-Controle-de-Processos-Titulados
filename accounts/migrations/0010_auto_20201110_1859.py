# Generated by Django 3.0 on 2020-11-10 21:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20201110_1853'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='interessado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Interessado'),
        ),
    ]