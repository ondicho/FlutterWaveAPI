import json

from django.shortcuts import render

# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from premium.models import Payment, Currency
from premium.serializers import PaymentSerializer
from rest_framework.response import Response
from django.http import JsonResponse
import urllib
import requests
from requests import Session
from django.utils.decorators import method_decorator

paymentRoute = "https://api.flutterwave.com/v3/payments/"


class SubscriptionPayment(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        tx_ref = request.POST.get("tx_ref")
        amount = request.POST.get("amount")
        redirect_url = request.POST.get("redirect_url")
        phoneNumber = request.POST.get("phoneNumber")
        payment_options = request.POST.get("payment_options")
        currency_code = request.POST.get("currency")

        code = Currency.objects.get(id=currency_code)
        currency = code.code

        load = {
            "tx_ref": tx_ref,
            "amount": amount,
            "currency": currency,
            "redirect_url": redirect_url,
            "payment_options": payment_options,
            "customer": {
                "email": request.user.email,
                "phonenumber": phoneNumber,
                "name": request.user.first_name + " " + request.user.last_name
            },
            "customizations": {
                "title": "Whip Music Internship Test",
                "description": "Good Stuff",
                "logo": "https://assets.piedpiper.com/logo.png"
            }
        }
        print(load)
        session = NoRebuildAuthSession()

        r = session.post(paymentRoute,
                         headers={'Authorization': "FLWSECK_TEST-ea5cbd800750cc4cf8158dd907a5aba4-X"},
                         data=load,
                         allow_redirects=False)
        # print(type(header))
        print(r)
        # print(r.status_code)
        print(r.json())

        # print(content)
        return self.create(request, *args, **kwargs)


class NoRebuildAuthSession(Session):
    def rebuild_auth(self, prepared_request, response):
        """
        No code here means requests will always preserve the Authorization
        header when redirected.
        Be careful not to leak your credentials to untrusted hosts!
        """
