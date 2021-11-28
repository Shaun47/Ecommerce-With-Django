from django.urls import path
from rest_framework import routers
from .views import HomeBanner,test,AboutUs,Services,Contact

router = routers.SimpleRouter()
router.register('home-banner', HomeBanner, basename='home-banner')
router.register('about-banner', AboutUs, basename='about-banner')
router.register('services-banner', Services, basename='services-banner')
router.register('contact-banner', Contact, basename='contact-banner')

urlpatterns = router.urls

#
# urlpatterns = [
#     path('test/',test),
# ]