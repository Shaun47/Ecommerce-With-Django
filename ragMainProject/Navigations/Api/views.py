from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, renderers
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, action
from .serializer import NavigationSerializer, SubMenuSerializer
from ..models import ParentNav, SubMenu
from rest_framework import viewsets


# @api_view(['GET', 'POST'])
# @permission_classes([AllowAny])
# class NavigationsViewSet(viewsets.GenericViewSet):
#
#     serializer_class = NavigationSerializer
#     permission_classes = [AllowAny]
#     queryset = ParentNav.objects.all()
#
#     def get_queryset(self):
#         return self.queryset
#
#     def list(self, request, *args, **kwargs):
#         navs = self.get_queryset()
#
#         return navs


# class NavList(viewsets.ViewSet):
#     permission_classes = [AllowAny]
#     queryset = ParentNav.objects.all()
#
#     def list(self, request):
#         serializer_class = NavigationSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)
#
#     def retrieve(self, request, pk=None):
#         nav = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = NavigationSerializer(nav)
#         return Response(serializer_class.data)

class ParentNavList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = NavigationSerializer
    queryset = ParentNav.objects.all()


class ChildNavList(viewsets.ModelViewSet):
    # permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    serializer_class = SubMenuSerializer
    queryset = SubMenu.objects.all()
