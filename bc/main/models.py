from django.db import models

class Products(models.Model):
    photo = models.ImageField(upload_to="photos", default=None, blank=True, null=True, verbose_name="Фото")
    price = models.IntegerField('Цена')
    name = models.CharField('Наименование записи', max_length = 200)

    class Meta:
        verbose_name = 'товар'
        verbose_name_plural = 'Товары'

    @property
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url