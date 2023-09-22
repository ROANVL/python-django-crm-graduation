#!/bin/bash


# Активация виртуального окружения Django
source /home/andrei/work/python/dcrm/virt/bin/activate

# Переход в каталог с проектом Django
cd /home/andrei/work/python/dcrm/co_crm

# Запуск Python скрипта для обработки товаров
python manage.py process_products

# Деактивация виртуального окружения Django
deactivate
