from kidwear.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'ven',VenVset,basename='ven')
router.register(r'rainyseason',RainySeasonVset,basename='cloths')

urlpatterns = router.urls