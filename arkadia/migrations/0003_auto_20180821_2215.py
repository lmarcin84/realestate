# Generated by Django 2.1 on 2018-08-21 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('arkadia', '0002_auto_20180821_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='property',
            old_name='offer_number',
            new_name='signature',
        ),
        migrations.RemoveField(
            model_name='property',
            name='choices',
        ),
        migrations.AddField(
            model_name='property',
            name='armament_plot',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Uzbrojenie działki'),
        ),
        migrations.AddField(
            model_name='property',
            name='coast',
            field=models.CharField(blank=True, choices=[(0, 'Lewobrzeze'), (1, 'Prawobrzeze')], max_length=20, null=True, verbose_name='Prawo/Lewobrzeze'),
        ),
        migrations.AddField(
            model_name='property',
            name='district',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Dzielnica'),
        ),
        migrations.AddField(
            model_name='property',
            name='estate',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Osiedle'),
        ),
        migrations.AddField(
            model_name='property',
            name='offer_status',
            field=models.CharField(blank=True, choices=[(0, 'Aktualna'), (1, 'Zawieszona'), (2, 'Nieaktualna')], max_length=20, null=True, verbose_name='Status oferty'),
        ),
        migrations.AddField(
            model_name='property',
            name='type_of_plot',
            field=models.CharField(blank=True, choices=[(0, 'Rekreacyjna'), (1, 'Rolna'), (2, 'Budowlana')], max_length=20, null=True, verbose_name='Rodzaj działki'),
        ),
        migrations.AlterField(
            model_name='property',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Ulica'),
        ),
        migrations.AlterField(
            model_name='property',
            name='city',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Miejscowość'),
        ),
        migrations.AlterField(
            model_name='property',
            name='property_type',
            field=models.CharField(blank=True, choices=[('dom', 'Dom'), ('mieszkanie', 'Mieszkanie'), ('lokal', 'Lokal'), ('działka', 'Działka'), ('obiekt', 'Obiekt')], max_length=50, null=True, verbose_name='Typ nieruchomości'),
        ),
        migrations.AlterField(
            model_name='property',
            name='transaction_type',
            field=models.CharField(blank=True, choices=[('sprzedaz', 'Sprzedaz'), ('wynajem', 'Wynajem')], max_length=20, null=True, verbose_name='Rodzaj transakcji'),
        ),
    ]
