from rest_framework.routers import DefaultRouter
from categoria.api.views import CategoriaViewSet


router= DefaultRouter()
router.register('categorias',CategoriaViewSet,basename='categoria')
urlpatterns = router.urls