from django.contrib import admin

from .models import Bill


@admin.register(Bill)
class BillAdmin(admin.ModelAdmin):
    list_display = ('client_name',
                    'client_org',
                    'account_number',
                    'sum',
                    'date',
                    'service')
