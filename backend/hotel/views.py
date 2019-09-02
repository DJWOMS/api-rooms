import json
from django.core import serializers
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.views.generic.base import View

from .models import HotelRooms


class RoomRecord(View):
    def get(self, request):
        rooms = list(HotelRooms.objects.values())
        data = json.dumps(rooms)
        # rooms = HotelRooms.objects.all()
        # data = serializers.serialize("json", rooms)
        # print(data)
        return JsonResponse(data, safe=False)
