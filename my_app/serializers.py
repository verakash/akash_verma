from rest_framework import serializers
from .models import testmodels


class testserializers(serializers.ModelSerializer):
    class Meta:
        model = testmodels
        fields = ['Name', 'Age']