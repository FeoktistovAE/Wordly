from django.shortcuts import render
# from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from wordly.users.models import User
from wordly.users.serializers import UserSerializer

# Create your views here.
class UsersIndexView(APIView):
    def get(self, request):
        queryset = User.objects.all()
        serializer_for_quetyset = UserSerializer(
            instance=queryset,
            many=True,
        )
        return Response(serializer_for_quetyset.data)


class UserCreateView(APIView):
    def post(self, request):
        serializer_for_writing = UserSerializer(data=request.data)
        serializer_for_writing.is_valid()
        serializer_for_writing.save()
        return Response(data=serializer_for_writing.data, status=status.HTTP_201_CREATED)