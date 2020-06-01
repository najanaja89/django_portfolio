from rest_framework import serializers

class RecentWorkSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    image = serializers.ImageField()
