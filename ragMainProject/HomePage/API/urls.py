from rest_framework import routers
from .views import DifferenceList, ChooseUsList, TopProductsList, RequestCallList, FooterList

router = routers.SimpleRouter()
router.register('different', DifferenceList, basename='different')
router.register('choose', ChooseUsList, basename='choose')
router.register('top-product', TopProductsList, basename='top-product')
router.register('request', RequestCallList, basename='request')
router.register('footer', FooterList, basename='footer')

urlpatterns = router.urls
