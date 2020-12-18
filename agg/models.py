from django.db import models

# Create your models here.


# 商品テーブルを用意

class Product(models.Model):
    name = models.CharField(verbose_name="商品名", max_length=255, null=False, blank=False)


class Product_Log(models.Model):
    date = models.DateField(verbose_name="日付", null=False, blank=False)
    product = models.ForeignKey(Product, verbose_name="商品", null=True, blank=False, on_delete=models.SET_NULL)
    amount = models.IntegerField(verbose_name="個数", null=False, blank=False)

