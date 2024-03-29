# Generated by Django 3.0 on 2021-09-10 22:10

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0027_auto_20210908_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='cadastrarr',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['F', 'Fácil'], ['M', 'Moderado'], ['D', 'Difícil']], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='localizacao',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['F', 'Fácil'], ['M', 'Moderado'], ['D', 'Difícil']], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='relatorio',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['S', 'Sim'], ['N', 'Não']], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='feedback',
            name='visualizacao',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['F', 'Fácil'], ['M', 'Moderado'], ['D', 'Difícil']], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='scpt',
            field=multiselectfield.db.fields.MultiSelectField(choices=[['S', 'Sim'], ['N', 'Não']], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='processo',
            name='interessado',
            field=models.ManyToManyField(to='accounts.Interessado'),
        ),
    ]
