from django.db import models


class Bill(models.Model):
    client_name = models.CharField(
        'Имя клиента',
        max_length=200,
    )
    client_org = models.CharField(
        'Организация клиента',
        max_length=200,
    )
    account_number = models.PositiveIntegerField(
        'Номер-счёт',
    )
    sum = models.DecimalField(
        'Сумма',
        decimal_places=2,
        max_digits=20,
    )
    date = models.DateTimeField(
        'Дата',
    )
    service = models.CharField(
        'Название сервиса',
        max_length=200,
    )

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'

    def __str__(self):
        return f'{self.date} | {self.account_number} | {self.sum}'
