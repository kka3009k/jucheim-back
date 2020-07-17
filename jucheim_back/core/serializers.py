import base64
import json
import smtplib
from collections import OrderedDict
from datetime import timedelta, datetime,date
from django.contrib.auth import get_user_model, hashers 
from django.core.files.base import ContentFile
from django.db.models import Model
from rest_framework import serializers
from rest_framework.utils import model_meta
from .models import *
import re


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('id', 'name')


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('__all__')

    def to_representation(self, instance):
        representation = super(ProductsSerializer, self).to_representation(instance)
        representation['category_name'] = CategorySerializer(instance.category).data
        #representation['credit_docs'] = CreditDoc.objects.filter(credit)
        return representation


class ProductInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = '__all__'

    def to_representation(self, instance):
        representation = super(ProductInfoSerializer, self).to_representation(instance)
        representation['category_name'] = CategorySerializer(instance.category).data
        representation['photos'] = PhotoProductsSerializer(instance.photo_product.all(),
                                                         many=True).data
        #representation['credit_docs'] = CreditDoc.objects.filter(credit)
        return representation

class PhotoProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhotoProducts
        fields = ('__all__')

class BannersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banners
        fields = ('__all__')


