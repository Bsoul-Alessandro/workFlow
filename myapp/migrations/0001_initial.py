# Generated by Django 5.0.4 on 2024-04-29 11:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidato',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('cognome', models.CharField(max_length=30)),
                ('tel', models.IntegerField()),
                ('residenza', models.CharField(max_length=30)),
                ('competenze', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Datore',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(max_length=30)),
                ('cognome', models.CharField(max_length=30)),
                ('tel', models.IntegerField()),
                ('azienda', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Messaggio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_mittente', models.IntegerField()),
                ('contenuto', models.CharField(max_length=50)),
                ('id_candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.candidato')),
                ('id_datore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.datore')),
            ],
        ),
        migrations.CreateModel(
            name='Offerta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descrizione', models.CharField(max_length=150)),
                ('data', models.DateTimeField()),
                ('requisiti', models.CharField(max_length=150)),
                ('id_datore', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.datore')),
            ],
        ),
        migrations.CreateModel(
            name='Candidatura',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stato', models.CharField(default='in sospeso', max_length=30)),
                ('id_candidato', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.candidato')),
                ('id_offerta', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.offerta')),
            ],
        ),
    ]
