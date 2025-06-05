from rest_framework import serializers
from .models import Student
class StudentSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    name = serializers.CharField()


    def create(self, validated_data):
        return Student.objects.create(**validated_data)

    def update(self, instance, validated_data):
        # instance.id = validated_data.get('id', instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance