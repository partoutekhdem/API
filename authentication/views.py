import random

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .tokens import account_activation_token
from .models import Client as ClientApp, Driver
from .serlializers import ClientSerializer, DriverSerializer
from infobip_channels.sms.channel import SMSChannel


# Create your views here.
@api_view(['POST'])
def send_code(request):

    BASE_URL = "https://zjlww2.api.infobip.com"
    API_KEY = "c300d4003cf7f0614d0cc258340905f4-8c59b9a0-9442-4cda-8f8b-88d679f80ce0"
    phone = request.data.get('phone')
    if phone:

        auth_code = str(random.randint(100000, 999999))
        message_body = f"Your authentication code is: {auth_code}"
        status_message=''
        try:
            channel = SMSChannel.from_auth_params(
                {
                    "base_url": BASE_URL,
                    "api_key": API_KEY,
                }
            )

            # Send a message with the desired fields.
            channel.send_sms_message(
                {
                    "messages": [
                        {
                            "destinations": [{"to": phone}],
                            "text": message_body,
                        }
                    ]
                }
            )

            # Get delivery reports for the message. It may take a few seconds show the just-sent message.
            query_parameters = {"limit": 10}
            delivery_reports = channel.get_outbound_sms_delivery_reports(query_parameters)
            print(delivery_reports)
            status_message=delivery_reports.status_code
        except Exception as e:
            print('An error occurred:', e)
            status_message=str(e)
        user = {
            "phone": phone,
            "code": auth_code
        }
        return Response(status=status.HTTP_200_OK, data={
            "code":auth_code,
            "status_message": status_message,
            "token": account_activation_token.make_token(user)
        })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def check_code(request):
    phone = request.data.get('phone')
    code = request.data.get('code')
    token = request.data.get('token')
    if phone and code and token:
        if account_activation_token.check_token({
            "phone": phone,
            "code": code,
        }, token=token):
            return Response(status=status.HTTP_200_OK, data={
                'auth': True
            })
        else:
            return Response(status=status.HTTP_200_OK, data={
                'auth': False
            })
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def get_data_user(request):
    phone = request.data.get('phone')
    if phone:
        user = ClientApp.objects.filter(phone=phone).first()
        if user:
            return Response(status=status.HTTP_200_OK, data={
                'type': 'Client',
                'obj': ClientSerializer(user).data
            })
        else:
            user = Driver.objects.filter(phone=phone).first();
            if user:
                return Response(status=status.HTTP_200_OK, data={
                    'type': 'Driver',
                    'obj': DriverSerializer(user).data
                })
            else:
                return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def save_date_client(request):
    client_serilizer = ClientSerializer(data=request.data)
    if client_serilizer.is_valid():
        client_serilizer.save()
        return Response(status=status.HTTP_200_OK, data=client_serilizer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def save_date_driver(request):
    driver_serilizer = DriverSerializer(data=request.data)
    if driver_serilizer.is_valid():
        driver_serilizer.save()
        return Response(status=status.HTTP_200_OK, data=driver_serilizer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
