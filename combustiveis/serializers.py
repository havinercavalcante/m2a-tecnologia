from rest_framework import serializers
from .models import Tanque, Bomba, Abastecimento

class TanqueSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanque
        fields = '__all__'

class BombaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bomba
        fields = '__all__'

class AbastecimentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Abastecimento
        fields = '__all__'
