# Generated by Django 3.2.8 on 2021-10-19 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_auto_20211019_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypUbrania',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typ', models.CharField(max_length=120)),
            ],
        ),
        migrations.AlterModelOptions(
            name='odziezdamska',
            options={'verbose_name': 'Odziez Damska', 'verbose_name_plural': 'Odziez Damska'},
        ),
        migrations.AlterModelOptions(
            name='odziezmeska',
            options={'verbose_name': 'Odziez Meska', 'verbose_name_plural': 'Odziez Meska'},
        ),
        migrations.AddField(
            model_name='odziezdamska',
            name='typ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.typubrania'),
        ),
        migrations.AddField(
            model_name='odziezmeska',
            name='typ',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.typubrania'),
        ),
    ]