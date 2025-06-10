from rest_framework import serializers
from .models import WatchList,StreamPlatform

class WatchListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=60)
    storyline = serializers.CharField(max_length=200)
    active = serializers.BooleanField(default=True)
    created = serializers.DateField()
    # platform = serializers.ForeignKey(StreamPlatform, on_delete= models.CASCADE)

    def create(self, validated_data):
        """
        Create and return a new `Watchlist` instance, given the validated data.
        """
        return WatchList.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Watchlist` instance, given the validated data.
        """
        instance.title = validated_data.get('title', instance.title)
        instance.storyline = validated_data.get('storyline', instance.storyline)
        instance.active = validated_data.get('active', instance.active)
        instance.created = validated_data.get('created', instance.created)
        instance.save()
        return instance


class StreamPlatformSerialize(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=70)
    about = serializers.CharField(max_length=100)
    website = serializers.URLField(max_length=100) 



    def create(self, validated_data):
        """
        Create and return a new `Stramplatform` instance, given the validated data.
        """
        return StreamPlatform.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Stramplatform` instance, given the validated data.
        """
        instance.name = validated_data.get('name', instance.name)
        instance.about = validated_data.get('about', instance.about)
        instance.website = validated_data.get('website', instance.website)
        instance.save()
        return instance