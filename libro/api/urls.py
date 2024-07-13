from rest_framework.routers import DefaultRouter
from libro.api.views import LibroViewSet


router= DefaultRouter()
router.register('libros',LibroViewSet,basename='libro')
urlpatterns = router.urls