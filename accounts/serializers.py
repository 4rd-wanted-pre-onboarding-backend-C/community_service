from rest_framework import serializers
from .models import User


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128,
        min_length=8,
        write_only=True
    )

    token = serializers.CharField(max_length=255, read_only=True)

    class Meta:
        model = User
        fields = [
            'username',
            'password',
            'gender',
            'age',
            'teamgroup_id',
            'token',
        ]

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            gender=validated_data['gender'],
            age=validated_data['age'],
            password=validated_data['password']
        )
