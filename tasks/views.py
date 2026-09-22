import json
import base64

from django.http import HttpRequest, JsonResponse
from django.contrib.auth import authenticate

from .models import Task


def tasks_view(request: HttpRequest) -> JsonResponse:
    auth = request.headers.get('Authorization')
    if not auth:
        return JsonResponse(
        data={
            "status": "error",
            "message": "user not found."
        },
        status=404
    )
    username, password = base64.b64decode(auth.split()[1]).decode().split(':')
    user = authenticate(request, username=username, password=password)

    if user is None:
        return JsonResponse(
            data={
                "status": "error",
                "message": "user not found."
            },
            status=404
        )

    if request.method == 'GET':
        tasks_list = []
        for task in user.tasks.all():
            tasks_list.append(task.to_dict())
        return JsonResponse(
            data={
                'tasks': tasks_list
            },
            status=200
        )
    elif request.method == 'POST':
        data = json.loads(request.body)

        task = Task(
            title=data['title'],
            description=data['description'],
            priority=data['priority'],
            user=user
        )
        task.save()
        return JsonResponse(
            data={
                'task': task.to_dict()
            },
            status=201
        )
