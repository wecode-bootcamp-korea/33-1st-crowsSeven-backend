# Generated by Django 4.0.4 on 2022-05-26 06:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('count', models.IntegerField(default=0)),
                ('shopping_fee', models.IntegerField(default=3000)),
                ('order_number', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'orders',
            },
        ),
        migrations.CreateModel(
            name='OrderItemStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_status', models.CharField(max_length=10)),
            ],
            options={
                'db_table': 'order_item_status',
            },
        ),
        migrations.CreateModel(
            name='OrderStatus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'order_status',
            },
        ),
        migrations.CreateModel(
            name='PaymentMethod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'payment_methods',
            },
        ),
        migrations.CreateModel(
            name='PresentDeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=300)),
                ('delivery_email', models.EmailField(max_length=254)),
                ('recipient', models.CharField(max_length=10)),
                ('receive_phonenumber', models.IntegerField()),
                ('delivery_message', models.TextField(max_length=200, null=True)),
            ],
            options={
                'db_table': 'present_delivery_addresses',
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipping_company', models.CharField(max_length=50)),
                ('shipping_number', models.CharField(max_length=100)),
                ('count', models.IntegerField(default=0)),
                ('option_product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.optionproduct')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.order')),
                ('order_item_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderitemstatus')),
            ],
            options={
                'db_table': 'order_items',
            },
        ),
        migrations.AddField(
            model_name='order',
            name='order_status',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.orderstatus'),
        ),
        migrations.AddField(
            model_name='order',
            name='present_delivery_address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.presentdeliveryaddress'),
        ),
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user'),
        ),
        migrations.CreateModel(
            name='DeliveryAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivery_address', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.user')),
            ],
            options={
                'db_table': 'delivery_addresses',
            },
        ),
    ]
