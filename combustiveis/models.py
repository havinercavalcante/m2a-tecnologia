from django.db import models

class Tanque(models.Model):
    TIPO_COMBUSTIVEL_CHOICES = [
        ('GASOLINA', 'Gasolina'),
        ('DIESEL', 'Óleo Diesel'),
    ]
    tipo_combustivel = models.CharField(max_length=10, choices=TIPO_COMBUSTIVEL_CHOICES)
    capacidade = models.FloatField()

    def __str__(self):
        return f'{self.tipo_combustivel} - {self.capacidade}L'

class Bomba(models.Model):
    tanque = models.ForeignKey(Tanque, related_name='bombas', on_delete=models.CASCADE)
    numero = models.IntegerField()

    def __str__(self):
        return f'Bomba {self.numero} - {self.tanque.tipo_combustivel}'

class Abastecimento(models.Model):
    bomba = models.ForeignKey(Bomba, related_name='abastecimentos', on_delete=models.CASCADE)
    data_hora = models.DateTimeField(auto_now_add=True)
    litros = models.FloatField()
    valor = models.FloatField()
    imposto = models.FloatField(default=0.0, editable=False)

    def save(self, *args, **kwargs):
        self.imposto = self.valor * 0.13 
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.data_hora} - Bomba {self.bomba.numero} - {self.litros}L - R${self.valor}'