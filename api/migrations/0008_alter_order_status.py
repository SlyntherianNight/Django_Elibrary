# Generated by Django 3.2 on 2021-07-26 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20210719_1518'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('out of delivery', 'out of delivery'), ('Delivered', 'Delivered')], max_length=200, null=True),
        ),
    ]
