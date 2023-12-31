# Generated by Django 3.2.16 on 2023-07-05 14:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmployerName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('middle_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='')),
                ('rate', models.DecimalField(decimal_places=2, max_digits=10)),
                ('age', models.PositiveSmallIntegerField()),
                ('department', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='departments.department')),
                ('full_name', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='employees.employername')),
                ('position', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employers', to='employees.position')),
            ],
        ),
    ]
