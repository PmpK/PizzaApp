# Generated by Django 3.0 on 2019-12-21 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_cart'),
    ]

    operations = [
        migrations.CreateModel(
            name='PizzaOnCart',
            fields=[
                ('pizzamenu_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='orders.PizzaMenu')),
                ('toppings', models.ManyToManyField(blank=True, to='orders.Topping')),
            ],
            bases=('orders.pizzamenu',),
        ),
    ]
