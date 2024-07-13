from rest_framework.routers import DefaultRouter
from autor.api.views import AutorViewSet


router= DefaultRouter()
router.register('autores',AutorViewSet,basename='autor')
urlpatterns = router.urls