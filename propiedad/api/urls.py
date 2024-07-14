from rest_framework.routers import DefaultRouter
from propiedad.api.views import PropiedadViewSet


router= DefaultRouter()
router.register('propiedades',PropiedadViewSet,basename='propiedad')
urlpatterns = router.urls