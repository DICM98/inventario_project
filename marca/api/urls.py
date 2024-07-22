from rest_framework.routers import DefaultRouter
from marca.api.views import MarcaViewSet


router= DefaultRouter()
router.register('marcas',MarcaViewSet,basename='marca')
urlpatterns = router.urls