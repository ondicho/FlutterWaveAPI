from django.db import models
import time
from django.contrib.auth.models import User


# Create your models here.
def paymentId():
    prefix = "PID"
    timestamp = str(int(time.time() * 10000000))
    default_value = prefix + timestamp
    return (default_value)


class Payment(models.Model):
    payment_choices = [
        ("account", "account"),
        ("card", "card"),
        ("banktransfer", "banktransfer"),
        ("mpesa", "mpesa"),
        ("mobilemoneyrwanda", "mobilemoneyrwanda"),
        ("mobilemoneyzambia", "mobilemoneyzambia"),
        ("qr", "qr"),
        ("mobilemoneyuganda", "mobilemoneyuganda"),
        ("ussd", "ussd"),
        ("credit", "credit"),
        ("barter", "barter"),
        ("mobilemoneyghana", "mobilemoneyghana"),
        ("payattitude", "payattitude"),
        ("mobilemoneyfranco", "mobilemoneyfranco"),
        ("paga", "paga"),
        ("1voucher", "1voucher"),
        ("mobilemoneytanzania", "mobilemoneytanzania")
    ]
    currency_choices = [('KES', 'KES'), ('USD', 'USD')]
    tx_ref = models.CharField(max_length=256, blank=False, null=False, default=paymentId)
    amount = models.IntegerField(blank=True, null=True)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    redirect_url = models.CharField(default="https://webhook.site/9d0b00ba-9a69-44fa-a43d-a82c33c36fdc",
                                    max_length=100)
    payment_options = models.CharField(choices=payment_choices, max_length=32)
    phoneNumber = models.BigIntegerField()
    payment_options = models.CharField(choices=payment_choices, max_length=32)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return str(self.code)
