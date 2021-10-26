from products.manager import ProductManager
from ecommerce.singnals_our import discount_applied

def send_promotional_offers(**kwargs):
    print("Promotional offers sent")

discount_applied.connect(receiver=send_promotional_offers, sender=ProductManager)
