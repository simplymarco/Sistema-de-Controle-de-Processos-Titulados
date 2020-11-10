# Generated by Django 3.0 on 2020-11-10 22:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_auto_20201110_1859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Setor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=200, null=True)),
                ('sigla', models.CharField(max_length=10, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='processo',
            name='interessado',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.Interessado'),
        ),
    ]
