from django.db import models

# Create your models here.
class NewArrivals(models.Model):
    title = models.CharField(
        max_length = 100,
        verbose_name = 'Название продукта'
    )
    description = models.TextField(
        verbose_name = 'Описание продукта'
    )
    image = models.ImageField(
        verbose_name = 'Изображение продукта',
        upload_to = 'product_image/'
    )

    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name = 'Новые поступления'
        verbose_name_plural = 'Новые поступления'