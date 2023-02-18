from django.db import models


CURRENCY_CHOICES = (
    ('usd', '$'),
    ('eur', '€')
)


class Item(models.Model):
    name = models.CharField('Название', max_length=50, help_text='Укажите имя товара')
    description = models.TextField('Описание', max_length=300, help_text='Введите описание товара')
    price = models.PositiveIntegerField('Цена', help_text='Укажите цену товара (в центах)')
    currency = models.CharField('Валюта', max_length=50, choices=CURRENCY_CHOICES, help_text='Выберите валюту')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.name

    def get_display_price(self):
        return '{0:.2f}'.format(self.price / 100)

    def get_price_in_euro(self):
        return '{0:.2f}'.format(self.price / 100 / 1.06)


class Order(models.Model):
    items = models.ManyToManyField(Item, related_name='items')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
