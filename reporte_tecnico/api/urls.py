from rest_framework.routers import DefaultRouter
from reporte_tecnico.api.views import Reporte_TecnicoViewSet


router= DefaultRouter()
router.register('reportes_tecnicos',Reporte_TecnicoViewSet,basename='reporte_tecnico')
urlpatterns = router.urls