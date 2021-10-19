# Generated by Django 3.2.8 on 2021-10-19 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='OdziezDamska',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=120)),
                ('rozmiar', models.CharField(max_length=4)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('kolor', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='OdziezMeska',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nazwa', models.CharField(max_length=120)),
                ('rozmiar', models.CharField(max_length=4)),
                ('cena', models.DecimalField(decimal_places=2, max_digits=4)),
                ('kolor', models.CharField(max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Ubranie',
        ),
    ]