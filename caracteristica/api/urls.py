from rest_framework.routers import DefaultRouter
from caracteristica.api.views import CaracteristicaViewSet


router= DefaultRouter()
router.register('caracteristicas',CaracteristicaViewSet,basename='caracteristica')
urlpatterns = router.urls