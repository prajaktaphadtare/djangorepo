from electronics.views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'product',ProductsVset,basename='product')
router.register(r'vendor',VendorVset,basename='vendor')

urlpatterns = router.urls