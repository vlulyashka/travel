from django.db import models
from django.utils import timezone

class Trip(models.Model):
    HOTEL_CLASS_CHOICES = [
        ('1', '1 звезда'),
        ('2', '2 звезды'),
        ('3', '3 звезды'),
        ('4', '4 звезды'),
        ('5', '5 звезд'),
    ]
    
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    attraction_image = models.ImageField(upload_to='attractions/', verbose_name='Изображение достопримечательности')
    days = models.PositiveIntegerField(verbose_name='Количество дней')
    trip_date = models.DateField(default=timezone.now, verbose_name='Дата поездки')
    hotel_class = models.CharField(max_length=1, choices=HOTEL_CLASS_CHOICES, verbose_name='Класс отеля')
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    
    def __str__(self):
        return f"{self.country}, {self.city} - {self.trip_date}"
    
    class Meta:
        verbose_name = 'Поездка'
        verbose_name_plural = 'Поездки'
        ordering = ['-trip_date']