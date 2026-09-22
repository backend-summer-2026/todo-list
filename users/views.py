import base64
import json
from datetime import datetime

from django.http import HttpRequest, JsonResponse
from django.contrib.auth.models import make_password
from django.contrib.auth import authenticate
from django.contrib.auth.models import User


def register_view(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse(
            data={
                'status': 'error',
                'message': 'method not allowed.'
            },
            status=404
        )

    data = json.loads(request.body)

    try:
        User.objects.get(username=data['username'])
        return JsonResponse(
            data={
                'status': 'error',
                'message': 'user already exists.'
            },
            status=400
        )
    except User.DoesNotExist:
        user = User(
            username=data['username'],
            email=data['email'],
            password=make_password(data['password']),
            first_name=data['first_name'],
            last_name=data['last_name'],
        )
        user.save()

        return JsonResponse(
            data={
                'status': 'success',
                'message': 'user has been created.'
            },
            status=201
        )


def login_view(request: HttpRequest) -> JsonResponse:
    if request.method != 'POST':
        return JsonResponse(
            data={
                'status': 'error',
                'message': 'method not allowed.'
            },
            status=404
        )

    auth = request.headers.get('Authorization').split()[1]

    username, password = base64.b64decode(auth).decode().split(':')

    user = authenticate(request, username=username, password=password)

    if user is not None:
        return JsonResponse(
            data={
                "status": "success",
                "message": "you have been loggen in."
            },
            status=200
        )
    return JsonResponse(
        data={
            "status": "error",
            "message": "user not found."
        },
        status=404
    )
