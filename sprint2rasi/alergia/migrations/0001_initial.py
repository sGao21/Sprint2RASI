# Generated by Django 3.2.6 on 2023-09-29 04:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('historiasclinicas', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo', models.CharField(max_length=20)),
                ('historiasociada', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='historiasclinicas.historiaclinica')),
            ],
        ),
    ]
