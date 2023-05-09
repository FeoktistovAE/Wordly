from rest_framework import serializers
from wordly.users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'get_full_name', 'username']
        extra_kwargs = {
            'username': {'write_only': True},
            'full_name': {'source': 'get_full_name', 'read_only': True}
        }
