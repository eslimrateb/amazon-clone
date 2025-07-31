import os , django 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()
from faker import Faker
from product.models import Product, Brand
from random import randint, seed

def seed_brands(n):
    fake = Faker()
    images=['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']
    for _ in range(n):
        Brand.objects.create(
            name=fake.name(),
            image=f'brand/{images[randint(0, len(images)-1)]}'
        )
    print(f"{n} brands seeded successfully.")

def seed_products(n):
    fake = Faker()
    images=['1.jpg', '2.jpg', '3.jpg', '4.jpg', '5.jpg', '6.jpg', '7.jpg', '8.jpg', '9.jpg', '10.jpg']
    brands = Brand.objects.all()
    for _ in range(n):
        Product.objects.create(
            name=fake.name(),
            flag=fake.word(ext_word_list=['New', 'Sale', 'Feature']),
            price=randint(10, 100),
            image=f'product/{images[randint(0, len(images)-1)]}',
            sku=randint(1000, 9999),
            subtitle=fake.text(max_nb_chars=100),
            description=fake.text(max_nb_chars=200),
            quantity=randint(1, 50),
            brand=brands[randint(0, len(brands)-1)]
        )
    print(f"{n} products seeded successfully.")
seed_products(5)