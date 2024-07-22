from rest_framework.routers import DefaultRouter
from clasificacion.api.views import ClasificacionViewSet


router= DefaultRouter()
router.register('clasificaciones',ClasificacionViewSet,basename='clasificacion')
urlpatterns = router.urls