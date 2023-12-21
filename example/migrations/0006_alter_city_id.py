# Generated by Django 4.1.3 on 2023-12-19 20:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('example', '0005_alter_user_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]