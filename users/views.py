import json
from datetime import datetime

from django.http import HttpRequest, JsonResponse

from .models import Account


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
        Account.objects.get(username=data['username'])
        return JsonResponse(
            data={
                'status': 'error',
                'message': 'account already exists.'
            },
            status=400
        )
    except Account.DoesNotExist:
        account = Account(
            username=data['username'],
            email=data['email'],
            password=data['password'],
            first_name=data['first_name'],
            last_name=data['last_name'],
            bio=data.get('bio'),
            birth_date=datetime.strptime(
                data['birth_date'],
                '%d.%m.%Y'
            ),
        )
        account.save()

        return JsonResponse(
            data={
                'status': 'success',
                'message': 'account has been created.'
            },
            status=201
        )
