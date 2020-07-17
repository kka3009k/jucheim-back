# Generated by Django 2.2.14 on 2020-07-16 16:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=1000, verbose_name='Наименование')),
                ('price', models.FloatField(verbose_name='Наименование')),
                ('category', models.ForeignKey(help_text='Категория продукта', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='category_product', to='core.Category')),
            ],
            options={
                'verbose_name': 'Продукты',
                'verbose_name_plural': 'Продукт',
            },
        ),
    ]
