# Generated by Django 3.2.16 on 2023-07-17 11:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('employees', '0004_alter_employername_last_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('employees', models.ManyToManyField(related_name='employee_project', to='employees.Employee')),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='projects', to='employees.employee')),
            ],
        ),
    ]
