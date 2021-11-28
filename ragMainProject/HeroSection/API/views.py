from django.http import HttpResponse
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets
from ..models import HomePage, AboutUs, Services, Contact
from .serializer import HomeSerializer


def test(request):
    return HttpResponse("hello")


class HomeBanner(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = HomeSerializer
    queryset = HomePage.objects.all()


class AboutUs(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = HomeSerializer
    queryset = AboutUs.objects.all()


class Services(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = HomeSerializer
    queryset = Services.objects.all()


class Contact(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = HomeSerializer
    queryset = Contact.objects.all()

