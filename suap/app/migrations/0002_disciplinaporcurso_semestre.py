# Generated by Django 4.2.4 on 2023-09-18 23:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='disciplinaporcurso',
            name='semestre',
            field=models.ForeignKey(default=11, on_delete=django.db.models.deletion.CASCADE, to='app.semestre'),
            preserve_default=False,
        ),
    ]
