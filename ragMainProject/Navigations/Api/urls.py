
from rest_framework import routers
from .views import ParentNavList,ChildNavList

router = routers.SimpleRouter()
router.register('menu',ParentNavList,basename='menu')
router.register('drop-menu',ChildNavList,basename='drop-menu')


urlpatterns = router.urls
