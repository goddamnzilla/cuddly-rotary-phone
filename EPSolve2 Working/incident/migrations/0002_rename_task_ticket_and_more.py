# Generated by Django 5.0.3 on 2024-03-28 12:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('incident', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Task',
            new_name='Ticket',
        ),
        migrations.RenameField(
            model_name='ticket',
            old_name='title',
            new_name='ticket_details',
        ),
    ]
