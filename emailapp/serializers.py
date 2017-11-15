from rest_framework import serializers
from .models import Person,Compose

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model=Person
        fields = ('name','email')


class ComposeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Compose
        fields = ('id','fromemail','sendto','subject','content')
