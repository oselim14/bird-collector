# Generated by Django 3.2.7 on 2021-11-02 21:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Sighting Date')),
                ('time', models.CharField(choices=[('AM', 'Morning'), ('PM', 'Afternoon')], default='AM', max_length=2)),
                ('bird', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.bird')),
            ],
        ),
    ]
