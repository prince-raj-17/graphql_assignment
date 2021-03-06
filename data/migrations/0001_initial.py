# Generated by Django 3.1.3 on 2021-05-29 05:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.BigIntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Name of the bank', max_length=49)),
            ],
            options={
                'db_table': 'Bank',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Branch',
            fields=[
                ('ifsc', models.CharField(help_text='IFSC code of branch', max_length=11, primary_key=True, serialize=False)),
                ('branch', models.CharField(help_text='Area of the branch is located', max_length=74)),
                ('address', models.CharField(help_text='Detailed address of the branch', max_length=195)),
                ('city', models.CharField(help_text='City where branch is located', max_length=50)),
                ('district', models.CharField(help_text='District where branch is located', max_length=50)),
                ('state', models.CharField(help_text='State in which branch is located', max_length=26)),
                ('bank', models.ForeignKey(help_text='FK to Bank table', on_delete=django.db.models.deletion.CASCADE, to='data.bank')),
            ],
            options={
                'db_table': 'Branch',
                'ordering': ['ifsc'],
            },
        ),
    ]
