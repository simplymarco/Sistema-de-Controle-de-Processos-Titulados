# Generated by Django 3.0 on 2020-11-06 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='terra',
            name='municipio',
            field=models.CharField(choices=[('Abreulândia', 'Abreulândia'), ('Aguiarnópolis', 'Aguiarnópolis'), ('Aliança do Tocantins', 'Aliança do Tocantins')], max_length=200, null=True),
        ),
    ]