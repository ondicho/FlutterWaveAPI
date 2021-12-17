from django.urls import path

from premium.views import SubscriptionPayment

urlpatterns = [
    path('payment/', SubscriptionPayment.as_view())
]
