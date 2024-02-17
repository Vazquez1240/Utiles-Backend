# Generated by Django 4.2.5 on 2023-09-25 08:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Utiles', '0005_alter_paquete_beneficiario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paquete',
            old_name='Beneficiario',
            new_name='beneficiario',
        ),
        migrations.AddField(
            model_name='beneficiario',
            name='numero_entrega',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='paquete',
            name='institucion',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='institucion', to='Utiles.escuela'),
            preserve_default=False,
        ),
    ]