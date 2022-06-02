from rest_framework import serializers
from .models import Entries

class Entries_serializer(serializers.ModelSerializer):
    # name=serializers.CharField(max_length=100)
    # price=serializers.IntegerField()
    # type=serializers.CharField(max_length=100)
    # desc=serializers.CharField(max_length=150)
    class Meta:
        model=Entries
        fields=['name','price','type','desc']

    def create(self,validated_data):
        return Entries.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name=validated_data.get('name',instance.name)    
        instance.price=validated_data.get('price',instance.price)    
        instance.type=validated_data.get('type',instance.type) 
        instance.desc=validated_data.get('desc',instance.desc) 
        instance.save()
        return instance     