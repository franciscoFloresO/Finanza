# Generated by Django 4.1.5 on 2024-03-15 13:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_financiera', '0005_alter_costo_costo_ceco_alter_costo_costo_cliente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='cliente_ceco',
            field=models.CharField(blank=True, default='', max_length=50, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_division',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='data_financiera.division'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_nombre',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='cliente_pais',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='pais_cliente', to='data_financiera.pais'),
        ),
    ]