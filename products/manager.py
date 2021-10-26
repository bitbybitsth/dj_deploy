from django.db.models import Manager
from ecommerce.singnals_our import discount_applied


class ProductManager(Manager):

    def get_samsung_products(self):
        return super().get_queryset().filter(brand__iexact='samsung')

    def apply_seasonal_discount(self, disc):
        discount_applied.send(sender=self.__class__)
        all_data = super().get_queryset().all()
        for data in all_data:
            data.price -= (data.price*disc)
        return all_data

    def get_taxed_prices(self):
        data = super().get_queryset().all()
        for da in data:
            da.price = da.price + (da.price*0.01)
        return data



