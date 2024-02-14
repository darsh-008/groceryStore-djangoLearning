# Generated by Django 5.0.1 on 2024-02-07 19:03

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='date_user',
        ),
        migrations.AddField(
            model_name='client',
            name='phone_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='description',
            field=models.TextField(blank=True, max_length=1000, null=True),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='client',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.client'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='myapp.item'),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='last_updated',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity_ordered',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AddField(
            model_name='orderitem',
            name='status',
            field=models.IntegerField(choices=[(0, 'cancelled'), (1, 'placed'), (2, 'shipped'), (3, 'delivered')], default=1),
        ),
        migrations.AlterField(
            model_name='client',
            name='city',
            field=models.CharField(choices=[('WD', 'Windsor'), ('TO', 'Toronto'), ('CH', 'Chatham'), ('WL', 'WATERLOO')], default='CH', max_length=2),
        ),
    ]