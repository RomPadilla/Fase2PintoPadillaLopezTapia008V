# Generated by Django 3.1.3 on 2020-11-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Registro', '0002_auto_20201107_2206'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Personaje',
            field=models.CharField(choices=[(1, 'Naruto'), (2, 'Sasuke'), (3, 'Gaara'), (4, 'Itachi'), (5, 'Kakashi'), (6, 'Sakura'), (7, 'Otro')], help_text='Seleccione su personaje favorito', max_length=16),
        ),
    ]