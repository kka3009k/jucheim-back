from django.shortcuts import render
import random
from io import StringIO
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from io import BytesIO
from datetime import date, timedelta
import time
from django.db.models import Count, Q, Sum
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.utils.decorators import method_decorator
from django.apps import apps
from django.conf import settings
from django.core.exceptions import ValidationError
from django_filters.rest_framework import DjangoFilterBackend
from django.http import HttpResponseNotFound
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.filters import SearchFilter
from rest_framework.generics import (ListCreateAPIView, RetrieveUpdateAPIView, ListAPIView,
                                     RetrieveUpdateDestroyAPIView, RetrieveAPIView,
                                     UpdateAPIView, DestroyAPIView, RetrieveAPIView, get_object_or_404, GenericAPIView)
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from email.mime.text import MIMEText
from email.header    import Header
import multiprocessing
from .serializers import *
from .models import * 
#import cv2
import os
from django.contrib.staticfiles.views import serve


class LargeResultsSetPagination(PageNumberPagination):
    page_size = 1000
    page_size_query_param = 'page_size'
    max_page_size = 10000
# Create your views here.

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    http_method_names = ['get','post','put','options']
    permission_classes = (AllowAny,)
    serializer_class = CategorySerializer

    def get_queryset(self):
        queryset = self.queryset           
        return queryset

class ProductsViewSet(ListAPIView):
    queryset = Products.objects.all()
    http_method_names = ['get','post','put','options']
    permission_classes = (AllowAny,)
    serializer_class = ProductsSerializer

    def get_queryset(self):
        queryset = self.queryset.filter(category = self.kwargs['pk'])           
        return queryset

class ProductInfoView(RetrieveUpdateAPIView):
    serializer_class = ProductInfoSerializer
    queryset = Products.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'name', )

    def get_queryset(self):
        queryset = self.queryset.filter(id = self.kwargs['pk'])           
        return queryset

class BannersView(viewsets.ModelViewSet):
    serializer_class = BannersSerializer
    queryset = Banners.objects.all()
    permission_classes = (AllowAny,)
    filter_backends = (DjangoFilterBackend, SearchFilter)
    search_fields = ('id', 'name', )

    def get_queryset(self):
        queryset = self.queryset        
        return queryset


class OrdersView(ListCreateAPIView):
    serializer_class = OrdersSerializer
    queryset = Orders.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        print(self.kwargs['cookie'])
        queryset = self.queryset.filter(user_coockie = self.kwargs['cookie']).order_by('-product')      
        return queryset

    def create(self, request, *args, **kwargs):
        order_data = {
            'product': request.data['id'],
            'user_coockie': request.data['coockie'],
            'quantity': request.data['quantity']
            }
        if Orders.objects.filter(user_coockie=request.data['coockie'], product = request.data['id']).exists():
            if request.data['quantity'] == 0:
                Orders.objects.filter(user_coockie=request.data['coockie'], product = request.data['id']).delete()
            else:
                order = Orders.objects.get(user_coockie=request.data['coockie'], product = request.data['id'])
                order.quantity = order.quantity + request.data['quantity']
                if order.quantity < 1:
                    order.quantity = 0
                order.save()
        else:
            serializer = self.get_serializer(data=order_data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        countOrders = Orders.objects.filter(user_coockie = request.data['coockie']).count()
        return Response(data = {'countOrders':countOrders} , status=201)




class GuestUserView(ListCreateAPIView):
    queryset = GuestUser.objects.all()
    permission_classes = (AllowAny,)

    def get_queryset(self):
        queryset = self.queryset 
        return queryset

    def create(self, request, *args, **kwargs):
        data = request.data
        user = None
        try :
            if data['userId']:
               user =  GuestUser.objects.get(id = data['userId'] )
            else:
               user = GuestUser.objects.create()
            return Response(data={'userId':user.id}, status=status.HTTP_201_CREATED)
        except Exception as ex:
           return Response(data="Error", status=status.HTTP_400_BAD_REQUEST)



    

   
