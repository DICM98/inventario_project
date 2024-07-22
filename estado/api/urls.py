from rest_framework.routers import DefaultRouter
from estado.api.views import EstadoViewSet


router= DefaultRouter()
router.register('estados',EstadoViewSet,basename='estado')
urlpatterns = router.urls