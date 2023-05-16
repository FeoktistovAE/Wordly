from rest_framework import serializers
from wordly.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'get_full_name', 'username', 'password']
        extra_kwargs = {
            'username': {'write_only': True},
            'password': {'write_only': True},
            'full_name': {'source': 'get_full_name', 'read_only': True},
        }

    def create(self, validated_data):
        user = User(
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name'],
            username = validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user