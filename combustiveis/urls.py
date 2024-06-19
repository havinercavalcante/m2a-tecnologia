from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TanqueViewSet, BombaViewSet, AbastecimentoViewSet

router = DefaultRouter()
router.register(r'tanques', TanqueViewSet)
router.register(r'bombas', BombaViewSet)
router.register(r'abastecimentos', AbastecimentoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
