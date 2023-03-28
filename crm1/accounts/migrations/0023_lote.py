# Generated by Django 4.1.7 on 2023-03-28 17:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0022_remove_cliente_date_created'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lote',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_lote', models.CharField(max_length=20, null=True)),
                ('fecha_lote', models.FloatField(blank=True, null=True)),
                ('estilo', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.estilo')),
            ],
        ),
    ]