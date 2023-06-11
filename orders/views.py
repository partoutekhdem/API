from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from .serializers import OrderSerializer, CallUserSerializer, CallChauffeurSerializer, PrivacyPolicySerializer, OfferSerializer
from .models import Order, Offer, ChauffeurCall, PrivacyPolicy, UserCall
from authentication.models import Client, Driver
from authentication.serlializers import ClientSerializer, DriverSerializer



@api_view(['POST'])
def save_date_order(request):
    order_serializer = OrderSerializer(data=request.data)
    if order_serializer.is_valid():
        order_serializer.save()
        return Response(status=status.HTTP_200_OK, data=order_serializer.data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST,data=order_serializer.errors)


@api_view(['POST'])
def get_order_by_type_vehicle(request):
    type = request.data.get('typeCar')
    if type:
        orders = Order.objects.filter(typeCar=type)
        if orders:
            return Response(data=OrderSerializer(orders, many=True).data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders(request):
    orders = Order.objects.all()
    if orders:
        return Response(data=OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def get_offers_by_orders(request):
    id = request.data.get('id_order')
    if id:
        order = Order.objects.filter(id=id).first()
        if order:
            offers = order.offers.all()
            if offers:
                return Response(OfferSerializer(offers, many=True).data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def upload_image_bay(request):
    order_id = request.data.get('order_id')
    image = request.data.get('image')
    if order_id:
        order = Order.objects.filter(id=order_id).first()
        if order:
            order.image_payment = image
            order.save()
            return Response(data={
                "image_urls":'/media/images/images_bay/' + order.image_payment.url
            })
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_canceled(request):
    orders = Order.objects.filter(status=Status.cancel)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_start_finish(request):
    orders = Order.objects.filter(status=Status.start_finish)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_start_done(request):
    orders = Order.objects.filter(status=Status.done)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_orders_normal(request):
    orders = Order.objects.filter(status=Status.normal)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
@api_view(['GET'])
def get_orders_start(request):
    orders = Order.objects.filter(status=Status.start)
    if orders:
        return Response(OrderSerializer(orders, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_all_client(request):
    clients = Client.objects.all()
    if clients:
        return Response(ClientSerializer(clients, many=True).data)

    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_drivers(request):
    drivers = Driver.objects.all()
    if drivers:
        return Response(DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['put'])
def update_client(request):
    id = request.data.get('id')
    if id:
        client = get_object_or_404(Client, id=id)
        client_serializer = ClientSerializer(client, data=request.data)
        if client_serializer.is_valid():
            client_serializer.save()
            return Response(data=client_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['put'])
def update_driver(request):
    id = request.data.get('id')
    if id:
        driver = get_object_or_404(Driver, id=id)
        driver_serilizer = DriverSerializer(driver,data=request.data)
        if driver_serilizer.is_valid():
            driver_serilizer.save()
            return Response(status=status.HTTP_200_OK, data=driver_serilizer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
            return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_old(request):
    drivers = Driver.objects.filter(active=True, subscribe=True, status=Status.accept)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


class Status:
    normal = 0
    start = 1
    start_finish = 2
    cancel = 3
    done = 4
    accept = 1
    under_review = 2
    reject = 0



@api_view(['GET'])
def get_driver_old_not_subscribe(request):
    drivers = Driver.objects.filter(active=True, subscribe=False, status=Status.accept)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_new(request):
    drivers = Driver.objects.filter(active=True, subscribe=True, status=Status.under_review)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_banned(request):
    drivers = Driver.objects.filter(active=False)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_driver_reject(request):
    drivers = Driver.objects.filter(status=Status.reject)
    if drivers:
        return Response(data=DriverSerializer(drivers, many=True).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def get_privacy_policy(req):
    privacy=PrivacyPolicy.objects.first()
    if privacy:
        return  Response(status=status.HTTP_200_OK,data=PrivacyPolicySerializer(privacy).data)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def get_ride(req):
    id=req.data.get('id')
    if id:
        order=Order.objects.filter(id=id).first()
        if order:
            return  Response(status=status.HTTP_200_OK,data=OrderSerializer(order).data)
        else:
            return  Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def update_order(req):
    id = req.data.get('id')
    if id:
        order = get_object_or_404(Order, id=id)
        order_serializer = OrderSerializer(order, data=req.data)
        if order_serializer.is_valid():
            order_serializer.save()
            return Response(data=order_serializer.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def update_rating_chauffeur(req):
    id=req.data.get('idDriver')
    rate=req.data.get('rating')
    if id and rate:
        chauffeur=Driver.objects.filter(id=id).first()
        if chauffeur:
            rateExit=(chauffeur.rating+float(rate))/2
            chauffeur.rating=rateExit
            chauffeur.save()
            return Response(status=status.HTTP_200_OK,data=DriverSerializer(chauffeur).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return  Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def add_offer(req):
    id=req.data.get('idOrder')
    offer=OfferSerializer(data=req.data)
    if id and offer.is_valid():
        offer.save()
        order=Order.objects.filter(id=id).first()
        if order:
            order.offers.add(Offer.objects.filter(id=offer.data['id']).first())
            order.save()
            return  Response(status=status.HTTP_200_OK,data=OrderSerializer(order).data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)
@api_view(['POST'])
def delete_offer(req):
    id_order = req.data.get('idOrder')
    id_offer=req.data.get('idOffer')
    if id_offer and id_order:
        order=Order.objects.filter(id=id_order).first()
        offer=Offer.objects.filter(id=id_offer).first()
        if order and offer:
            offer.delete()
            return Response(status=status.HTTP_200_OK,data=OrderSerializer(order).data)
        else: return Response(status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_call_user(request):
    calls=UserCall.objects.all()
    userCalls=CallUserSerializer(calls,many=True).data
    return Response(status=status.HTTP_200_OK,data=userCalls)

@api_view(['GET'])
def get_call_chauffeur(request):
    data=ChauffeurCall.objects.all()
    userCalls=CallChauffeurSerializer(data,many=True)
    return Response(status=status.HTTP_200_OK,data=userCalls.data)
