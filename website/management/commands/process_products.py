from django.core.management.base import BaseCommand
from website.models import Product, ProductOrder


class Command(BaseCommand):
    help = 'Process products and update purchase_needed field'

    def handle(self, *args, **kwargs):
        products = Product.objects.all()

        for product in products:
            if product.quantity < product.minimum_stock_level:
                product.purchase_needed = True
            else:
                product.purchase_needed = False

            product.save()

            # Попытка найти существующую запись ProductOrder для данного продукта
            product_order = ProductOrder.objects.filter(
                product=product).first()

            if product.purchase_needed:
                # Создаем или обновляем запись ProductOrder
                new_quantity_to_order = product.maximum_stock_level - product.quantity

                if product_order:
                    # Проверяем, изменилось ли количество
                    if new_quantity_to_order != product_order.quantity_to_order:
                        product_order.quantity_to_order = new_quantity_to_order
                        product_order.save()
                else:
                    # Создание новой записи
                    ProductOrder.objects.create(
                        product=product, quantity_to_order=new_quantity_to_order)
            elif product_order:
                # Если purchase_needed стало False, и запись существует, удаляем ее
                product_order.delete()

        self.stdout.write(self.style.SUCCESS(
            'Successfully processed products'))
