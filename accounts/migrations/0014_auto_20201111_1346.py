# Generated by Django 3.0 on 2020-11-11 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20201110_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='processo',
            name='dataTitulo',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='folha',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='interessado',
            field=models.ManyToManyField(to='accounts.Interessado'),
        ),
        migrations.AlterField(
            model_name='processo',
            name='livro',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='numeroTitulo',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]