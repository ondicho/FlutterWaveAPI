# Generated by Django 3.2.5 on 2021-12-16 22:10

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('code', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('trx_ref', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('amount', models.IntegerField(blank=True, null=True)),
                ('phoneNumber', models.BigIntegerField()),
                ('payment_options', models.CharField(choices=[('account', 'account'), ('card', 'card'), ('banktransfer', 'banktransfer'), ('mpesa', 'mpesa'), ('mobilemoneyrwanda', 'mobilemoneyrwanda'), ('mobilemoneyzambia', 'mobilemoneyzambia'), ('qr', 'qr'), ('mobilemoneyuganda', 'mobilemoneyuganda'), ('ussd', 'ussd'), ('credit', 'credit'), ('barter', 'barter'), ('mobilemoneyghana', 'mobilemoneyghana'), ('payattitude', 'payattitude'), ('mobilemoneyfranco', 'mobilemoneyfranco'), ('paga', 'paga'), ('1voucher', '1voucher'), ('mobilemoneytanzania', 'mobilemoneytanzania')], max_length=32)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='premium.currency')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
