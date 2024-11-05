from django.urls import path
from .views import QuoteView

urlpatterns = [
    path('send-quote/', QuoteView.as_view(), name='send_quote'),
]
