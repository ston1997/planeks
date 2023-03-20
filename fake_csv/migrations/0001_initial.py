# Generated by Django 4.1.7 on 2023-03-18 12:14

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Schema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('delimiter', models.CharField(choices=[(',', 'Comma (,)'), (';', 'Semicolon (;)'), ('\t', 'Tab (\t)'), (' ', 'Space ( )'), ('|', 'Vertical bar (|)')], default=',', help_text='column separator', max_length=1)),
                ('quote_character', models.CharField(choices=[('"', 'Double-quote (")'), ("'", "Single-quote (')")], default='"', max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='DataSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('Ready', 'READY'), ('Processing', 'PROCESSING')], default='Processing', max_length=10)),
                ('file', models.FileField(blank=True, null=True, upload_to='')),
                ('number_of_rows', models.PositiveIntegerField()),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fake_csv.schema')),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Column',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('data_type', models.CharField(choices=[('full_name', 'Full Name'), ('job', 'Job'), ('email', 'Email'), ('domain_name', 'Domain Name'), ('phone_number', 'Phone Number'), ('company_name', 'Company Name'), ('text', 'Text'), ('integer', 'Integer'), ('address', 'Address'), ('date', 'Date')], max_length=12)),
                ('order', models.PositiveSmallIntegerField()),
                ('data_range_from', models.IntegerField(blank=True, null=True, verbose_name='from')),
                ('data_range_to', models.IntegerField(blank=True, null=True, verbose_name='to')),
                ('schema', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='columns', to='fake_csv.schema')),
            ],
            options={
                'ordering': ('order',),
            },
        ),
    ]