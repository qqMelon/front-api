from rest_framework import serializers
from WarUnicorn.models import Unicorn


class UnicornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unicorn
        fields = ["id", "name", "model", "price", "available", "img_url"]

    def create(self, validated_data):
        return Unicorn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.color = validated_data.get("color", instance.color)
        instance.model = validated_data.get("model", instance.model)
        instance.price = validated_data.get("price", instance.price)
        instance.img_url = validated_data.get("img_url", instance.img_url)
        instance.available = validated_data.get("available", instance.available)
        instance.save()
        return instance
