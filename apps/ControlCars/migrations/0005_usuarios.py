# Generated by Django 3.0.5 on 2020-08-15 01:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ControlCars', '0004_auto_20200811_2232'),
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(help_text='Cédula o RUC', max_length=13)),
                ('telefono', models.CharField(blank=True, max_length=20, null=True)),
                ('ciudad', models.CharField(max_length=50)),
                ('img_perfil', models.ImageField(blank=True, null=True, upload_to='imgPerfil')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='usuario', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'usuarios',
                'verbose_name_plural': 'Usuarios',
            },
        ),
    ]
