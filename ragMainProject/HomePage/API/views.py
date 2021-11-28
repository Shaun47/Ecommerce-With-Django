from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializer import DifferenceSerializer,ChooseUsSerializer,TopProductsSerializer,RequestCallSerializer,FooterSerializer
from ..models import Difference, ChooseUs, TopProducts, RequestCall, Footer
from rest_framework import viewsets


class DifferenceList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = DifferenceSerializer
    queryset = Difference.objects.all()


class ChooseUsList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = ChooseUsSerializer
    queryset = ChooseUs.objects.all()


class TopProductsList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = TopProductsSerializer
    queryset = TopProducts.objects.all()


class RequestCallList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = RequestCallSerializer
    queryset = RequestCall.objects.all()


class FooterList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = FooterSerializer
    queryset = Footer.objects.all()