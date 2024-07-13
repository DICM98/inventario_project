from rest_framework.routers import DefaultRouter
from genero.api.views import GeneroViewSet


router= DefaultRouter()
router.register('generos',GeneroViewSet,basename='genero')
urlpatterns = router.urls