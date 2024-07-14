from rest_framework.routers import DefaultRouter
from tipo_movimiento.api.views import Tipo_MovimientoViewSet


router= DefaultRouter()
router.register('tipos_movimientos',Tipo_MovimientoViewSet,basename='tipo_movimiento')
urlpatterns = router.urls