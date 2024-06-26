# Generated by Django 5.0.4 on 2024-05-01 16:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='candidato',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='datore',
            name='tel',
        ),
        migrations.AddField(
            model_name='candidato',
            name='email',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='candidato',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='candidato',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='datore',
            name='email',
            field=models.CharField(max_length=60, null=True),
        ),
        migrations.AddField(
            model_name='datore',
            name='password',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='datore',
            name='username',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='cognome',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='competenze',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='nome',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='candidato',
            name='residenza',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='id_offerta',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.offerta'),
        ),
        migrations.AlterField(
            model_name='candidatura',
            name='stato',
            field=models.CharField(default='in sospeso', max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='datore',
            name='azienda',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='datore',
            name='cognome',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='datore',
            name='nome',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='messaggio',
            name='contenuto',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='messaggio',
            name='id_candidato',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.candidato'),
        ),
        migrations.AlterField(
            model_name='messaggio',
            name='id_datore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.datore'),
        ),
        migrations.AlterField(
            model_name='messaggio',
            name='id_mittente',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='offerta',
            name='data',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='offerta',
            name='descrizione',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='offerta',
            name='id_datore',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.datore'),
        ),
        migrations.AlterField(
            model_name='offerta',
            name='requisiti',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
