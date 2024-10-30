from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
@api_view(['POST'])
def logout_view(request):
    user = request.user
    user.auth_token.delete()
    return Response(status=status.HTTP_200_OK)


@api_view(['GET'])
def get_user_id(request):
    return Response(request.user.id)
