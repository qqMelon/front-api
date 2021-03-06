# Generated by Django 2.2.6 on 2019-10-18 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WarUnicorn', '0003_auto_20191017_1152'),
    ]

    operations = [
        migrations.AddField(
            model_name='unicorn',
            name='img_url',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name="Url de l'image"),
        ),
        migrations.AlterField(
            model_name='unicorn',
            name='available',
            field=models.BooleanField(verbose_name='Disponible'),
        ),
        migrations.AlterField(
            model_name='unicorn',
            name='color',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Couleur'),
        ),
        migrations.AlterField(
            model_name='unicorn',
            name='created',
            field=models.DateTimeField(auto_now_add=True, verbose_name='Date de création'),
        ),
        migrations.AlterField(
            model_name='unicorn',
            name='model',
            field=models.CharField(max_length=255, verbose_name='Modele'),
        ),
        migrations.AlterField(
            model_name='unicorn',
            name='name',
            field=models.CharField(blank=True, default='', max_length=255, null=True, verbose_name='Nom'),
        ),
        migrations.AlterField(
            model_name='unicorn',
            name='price',
            field=models.FloatField(verbose_name='Prix'),
        ),
    ]
