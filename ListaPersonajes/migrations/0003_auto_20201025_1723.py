# Generated by Django 3.1.2 on 2020-10-25 20:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ListaPersonajes', '0002_auto_20201025_0946'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookinstance',
            name='book',
        ),
        migrations.DeleteModel(
            name='Book',
        ),
        migrations.DeleteModel(
            name='BookInstance',
        ),
        migrations.DeleteModel(
            name='Genre',
        ),
    ]
