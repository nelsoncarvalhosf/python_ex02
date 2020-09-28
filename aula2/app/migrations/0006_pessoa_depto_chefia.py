# Generated by Django 3.1 on 2020-08-14 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_pessoa_hist_deptos'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='depto_chefia',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.RESTRICT, related_name='chefia_depto', to='app.departamento'),
        ),
    ]
