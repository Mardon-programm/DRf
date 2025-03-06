from rest_framework.routers import DefaultRouter
from apps.product.views import ProductMixins

router = DefaultRouter()
router.register(r"product", ProductMixins, basename="product")

urlpatterns = router.urls