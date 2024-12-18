from rest_framework import serializers
from . models import *

class MyModelSerializers(serializers.ModelSerializer):
    class Meta:
        model = book_appoinment_table
        fields = '__all__'