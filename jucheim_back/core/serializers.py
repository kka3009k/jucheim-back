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
