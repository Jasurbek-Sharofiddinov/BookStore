from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, )
        super().save(*args, **kwargs)


class Book(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, blank=True)
    picture = models.ImageField()
    description = models.TextField()
    author = models.CharField(max_length=200)
    publish_data = models.DateField()
    price = models.CharField(max_length=200)
    discount = models.CharField(max_length=200)
    rate = models.PositiveIntegerField()
    total = models.IntegerField()
    left_item = models.IntegerField()
    sold_out = models.IntegerField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        value = self.name
        self.slug = slugify(value, )
        super().save(*args, **kwargs)


class User(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    book_numbers = models.IntegerField()


class Order(models.Model):
    pending = 'P'
    complete = 'C'
    Ordering_status = [
        (pending, 'Pending'),
        (complete, 'Complete')
    ]
    ordering = models.CharField(max_length=1, choices=Ordering_status)
    customer = models.ForeignKey(User, on_delete=models.CASCADE)


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Book, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField()
