# Generated by Django 4.1.5 on 2024-03-13 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_financiera', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabla',
            fields=[
                ('id_tabla', models.AutoField(primary_key=True, serialize=False)),
                ('tabla_pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_financiera.pais')),
            ],
        ),
    ]
