from django.db import models
import uuid
from django.contrib.auth.models import User


# Create your models here.

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
    trx_ref = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    currency = models.ForeignKey('Currency', on_delete=models.PROTECT)
    amount = models.IntegerField(blank=True, null=True)
    phoneNumber = models.BigIntegerField()
    payment_options = models.CharField(choices=payment_choices, max_length=32)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class Currency(models.Model):
    code = models.CharField(max_length=3)

    def __str__(self):
        return str(self.code)
