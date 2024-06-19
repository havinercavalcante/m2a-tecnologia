from django.test import TestCase, Client
from django.urls import reverse
from .models import Tanque, Bomba, Abastecimento

class AbastecimentoViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.tanque_gasolina = Tanque.objects.create(tipo_combustivel='GASOLINA', capacidade=10000)
        self.bomba1 = Bomba.objects.create(tanque=self.tanque_gasolina, numero=1)
        self.bomba2 = Bomba.objects.create(tanque=self.tanque_gasolina, numero=2)
    
    def test_registrar_abastecimento(self):
        response = self.client.post(reverse('abastecimento-list'), {
            'bomba': self.bomba1.id,
            'litros': 50,
            'valor': 200,
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(Abastecimento.objects.count(), 1)
        self.assertEqual(Abastecimento.objects.first().valor, 200)

    def test_listar_abastecimentos(self):
        Abastecimento.objects.create(bomba=self.bomba1, litros=50, valor=200)
        Abastecimento.objects.create(bomba=self.bomba2, litros=30, valor=120)
        
        response = self.client.get(reverse('abastecimento-list'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 2)
