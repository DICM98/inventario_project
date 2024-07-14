from rest_framework.routers import DefaultRouter
from area_responsible.api.views import Area_ResponsibleViewSet


router= DefaultRouter()
router.register('area_responsibles',Area_ResponsibleViewSet,basename='area_responsible')
urlpatterns = router.urls