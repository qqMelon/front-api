from rest_framework import serializers
from WarUnicorn.models import User, UserProfile, Unicorn


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ("address", "photo")


class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ["url", "email", "first_name", "last_name", "password", "profile"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        profile_data = validated_data.pop("profile")
        password = validated_data.pop("password")
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get(
            "first_name", instance.first_name)
        instance.last_name = validated_data.get(
            "last_name", instance.last_name)
        instance.email = validated_data.get("email", instance.email)

        profile_data = validated_data.pop("profile")
        profile = instance.profile

        instance.save()
        profile.address = profile_data.get("address", profile.address)
        profile.photo = profile_data.get("photo", profile.photo)
        profile.save()

        return instance


class UnicornSerializer(serializers.ModelSerializer):
    class Meta:
        model = Unicorn
        fields = ["id", "name", "color", "model", "price", "img_url", "available"]

    def create(self, validated_data):
        return Unicorn.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.color = validated_data.get("color", instance.color)
        instance.model = validated_data.get("model", instance.model)
        instance.price = validated_data.get("price", instance.price)
        instance.img_url = validated_data.get("img_url", instance.available)
        instance.available = validated_data.get("available", instance.available)
        instance.save()
        return instance
