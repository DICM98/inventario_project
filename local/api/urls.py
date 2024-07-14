from rest_framework.routers import DefaultRouter
from local.api.views import LocalViewSet


router= DefaultRouter()
router.register('locals',LocalViewSet,basename='local')
urlpatterns = router.urls