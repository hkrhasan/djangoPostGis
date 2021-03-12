from django.db import connection
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from datetime import datetime, timezone, timedelta


class TestView(APIView):
    permission_classes = (permissions.AllowAny,)
    
    def post(self, request):
        lat = request.data['lat']
        lng = request.data['lng']

        query = f"SELECT ST_Contains(geom, ST_GeomFromText('POINT({lng} {lat})',26918)) FROM randomhamaraarea"

        cursor = connection.cursor()
        cursor.execute(query)
        r = cursor.fetchone()
        print("Result >>", r[0])
        print("latlng>>>", lat, lng)
        return Response({'valid': r[0]})