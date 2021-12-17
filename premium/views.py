from django.shortcuts import render

# Create your views here.
from rest_framework import generics, mixins
from rest_framework.permissions import IsAuthenticated

from premium.models import Payment
from premium.serializers import PaymentSerializer

paymentRoute = "https://api.flutterwave.com/v3/payments"


class SubscriptionPayment(mixins.ListModelMixin,
                          mixins.CreateModelMixin,
                          generics.GenericAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
