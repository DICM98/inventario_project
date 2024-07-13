from rest_framework.routers import DefaultRouter
from estudiante.api.views import EstudianteViewSet


router= DefaultRouter()
router.register('estudiantes',EstudianteViewSet,basename='estudiante')
urlpatterns = router.urls