from django.db import models
from django.contrib.auth.models import AbstractUser

CAIXA_CHOICES = (
    ('frios', 'frios'),
    ('presente', 'presente'),
    ('entrega', 'entrega'),
)

# Create your models here.
class User(AbstractUser):
    ''' user model '''

    def __str__(self):
        return self.username

class Caixas(models.Model):
    ''' caixas model '''
    number = models.IntegerField(help_text="Número de identificação do caixa")
    available = models.BooleanField(default=True) # disponivel
    line = models.IntegerField(help_text="Número de pessoas na fila") # fila
    waiting_time = models.IntegerField(help_text="Tempo de espera") # tempo de espera
    option = models.CharField(max_length=24, choices=CAIXA_CHOICES, default="presente")

    def __str__(self):
        return f"caixa {self.number}"


    def get_frios_all(self):
        return self.caixa_set.all()


    def get_caixas(self):
        ''' Retorna todos os caixas '''
        return self.caixas_set.all()


class Product(models.Model):
    name = models.CharField(max_length=120)
    price = models.FloatField()
    discount = models.FloatField()

    def price_with_discount(self):
        ''' Mostra o preço após aplicar o desconto '''
        return self.price - self.discount

    def __str__(self):
        return self.name