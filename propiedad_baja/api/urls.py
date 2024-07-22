from rest_framework.routers import DefaultRouter
from propiedad_baja.api.views import Propiedad_BajaViewSet


router= DefaultRouter()
router.register('propiedades_bajas',Propiedad_BajaViewSet,basename='propiedad_baja')
urlpatterns = router.urls