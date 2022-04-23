# Generated by Django 4.0 on 2022-04-21 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('edutech_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassNumber',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Number', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50)),
                ('Description', models.TextField(max_length=100)),
                ('subject', models.ManyToManyField(to='edutech_app.Subject')),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.TextField(max_length=50)),
                ('Description', models.TextField(max_length=100)),
                ('classNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edutech_app.classnumber')),
                ('subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edutech_app.subject')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='edutech_app.teacher')),
            ],
        ),
    ]
