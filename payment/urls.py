from django.urls import path
from . import views


urlpatterns = [
    path('create/', views.PaymentGateway.as_view(), name='payment_create'),
    path('Success/', views.success),
    path('Failure/', views.failure),
    path('thankyou/', views.thankyou, name='thankyou'),
]
