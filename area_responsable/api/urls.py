from rest_framework.routers import DefaultRouter
from area_responsable.api.views import Area_ResponsableViewSet


router= DefaultRouter()
router.register('area_responsables',Area_ResponsableViewSet,basename='area_responsable')
urlpatterns = router.urls