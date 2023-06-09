# Generated by Django 4.1.7 on 2023-04-01 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripCategoria', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'categorias',
                'verbose_name_plural': 'categorias de productos',
            },
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300, null=True)),
                ('precioUnitario', models.DecimalField(decimal_places=2, max_digits=8)),
                ('unidad', models.CharField(max_length=10)),
                ('existencia', models.IntegerField(null=True)),
                ('imgGrande', models.ImageField(null=True, upload_to='productos')),
                ('imgPeque', models.ImageField(null=True, upload_to='iconos')),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appProductos.categoria')),
            ],
        ),
    ]
