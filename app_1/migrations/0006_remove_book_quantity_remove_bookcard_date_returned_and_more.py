# Generated by Django 4.1.5 on 2023-02-02 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_1', '0005_bookshelfauthor_remove_bookcard_status_book_quantity_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='quantity',
        ),
        migrations.RemoveField(
            model_name='bookcard',
            name='date_returned',
        ),
        migrations.RemoveField(
            model_name='bookcard',
            name='date_took',
        ),
        migrations.RemoveField(
            model_name='bookcard',
            name='loan_days_num',
        ),
        migrations.AddField(
            model_name='bookcard',
            name='is_taken',
            field=models.BooleanField(default=False),
        ),
    ]
