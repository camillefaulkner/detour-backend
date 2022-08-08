import os
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
import requests
from rest_framework.decorators import action
# from rest_framework import status


class YELPView(ViewSet):

    @action(methods=["get"], detail=False)
    def yelp_api(self, request):
        yelp = os.environ.get('YELP_SECRET_KEY')
        headers = { 'Authorization': f'Bearer {yelp}', 'withCredentials': 'true'}
        lat = request.query_params.get('lat', None)
        long = request.query_params.get('long', None)

        r = requests.get(f'https://api.yelp.com/v3/businesses/search?&categories=coffee&open_now=true&limit=4&latitude={lat}&longitude={long}', headers=headers).json()

        return Response(r)
