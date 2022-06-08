# Generated by Django 4.0.4 on 2022-06-08 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Produse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod_produs', models.CharField(max_length=100)),
                ('descriere', models.CharField(max_length=100)),
                ('active', models.BooleanField(default=1)),
                ('pret_altex', models.CharField(max_length=100)),
                ('pret_emag', models.CharField(max_length=100)),
                ('imagine', models.ImageField(blank=True, null=True, upload_to='')),
                ('url_altex', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
