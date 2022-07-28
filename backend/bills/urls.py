from django.urls import path

from . import views

urlpatterns = [
        path("parse_bills/", views.parse_bills, name="parse_bills"),
        path("bills/", views.BillsAPIView.as_view(), name="bills"),
]
