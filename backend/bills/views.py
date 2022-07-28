from rest_framework.generics import ListAPIView
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import BillSerializer
from .models import Bill
from .utils import get_bills_list


@api_view(['POST'])
def parse_bills(request):
    bills = get_bills_list()
    if bills is not None:
        for bill in bills:
            try:
                Bill.objects.create(
                    client_name=bill['client_name'],
                    client_org=bill['client_org'],
                    account_number=bill['№'],
                    sum=bill['sum'],
                    date=bill['date'],
                    service=bill['service'],
                )
            except:
                pass
        return Response({'result': 'Bills successfully parsed'},
                        status=status.HTTP_201_CREATED)
    return Response({'result': 'Error occured'},
                    status=status.HTTP_400_BAD_REQUEST)


class BillsAPIView(ListAPIView):
    queryset = Bill.objects.all()
    serializer_class = BillSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['client_name','client_org']
