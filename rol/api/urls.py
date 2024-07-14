from rest_framework.routers import DefaultRouter
from rol.api.views import RolViewSet


router= DefaultRouter()
router.register('roles',RolViewSet,basename='rol')
urlpatterns = router.urls