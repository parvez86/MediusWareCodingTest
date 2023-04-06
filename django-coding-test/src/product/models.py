from django.db import models
from config.g_model import TimeStampMixin


# Create your models here.
class Variant(TimeStampMixin):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title


class Product(TimeStampMixin):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    title = models.CharField(max_length=255)
    sku = models.SlugField(max_length=255, unique=True)
    description = models.TextField()

    def __str__(self):
        return self.title


class ProductImage(TimeStampMixin):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    file_path = models.URLField(max_length=255)
    thumbnail = models.BooleanField(default=True)

    def __str__(self):
        return str(self.id)


class ProductVariant(TimeStampMixin):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    variant_title = models.CharField(max_length=255)
    variant = models.ForeignKey(Variant, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return self.variant_title


class ProductVariantPrice(TimeStampMixin):
    id = models.PositiveBigIntegerField(max_length=20, primary_key=True)
    product_variant_one = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_one')
    product_variant_two = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                            related_name='product_variant_two')
    product_variant_three = models.ForeignKey(ProductVariant, on_delete=models.CASCADE, null=True,
                                              related_name='product_variant_three')
    price = models.FloatField()
    stock = models.IntegerField(max_length=11)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.id)
