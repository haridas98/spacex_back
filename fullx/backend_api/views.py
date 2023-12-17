from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import NavbarItem, Adv
from .serializer import NavbarItemSerializer, AdvSerializer
from rest_framework.response import Response

class NavbarItemView(APIView):
    def get(self, request):
        navbar_items = NavbarItem.objects.all()
        serializer = NavbarItemSerializer(navbar_items, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = NavbarItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

class AdvView(APIView):
    def get(self, request):
        adv_objects = Adv.objects.all()
        serializer = AdvSerializer(adv_objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = AdvSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)