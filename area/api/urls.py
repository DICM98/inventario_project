from rest_framework.routers import DefaultRouter
from area.api.views import AreaViewSet


router= DefaultRouter()
router.register('areas',AreaViewSet,basename='area')
urlpatterns = router.urls