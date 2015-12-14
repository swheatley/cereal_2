from rest_framework import serializers
from main.models import Cereal  


class CerealSerializer(serializers.Serializer):
    cereal_name = serializers.CharField(max_length=200, null=True, blank=True)
    sugars = models.IntegerField(null=True, blank=True)
   
    def create(self, validated_data):
        return Cereal.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.cereal_name = validated_data.get('cereal_name', instance.cereal_name)
        instance.sugars = validated_data.get('sugars',)
        instance.save()
        return instance

