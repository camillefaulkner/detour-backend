# from rest_framework.viewsets import ViewSet
# from rest_framework.response import Response
# import requests
# from rest_framework import status
# from detourapi.models import DetourUser
# from detourapi.models.doc import Doc
# from detourapi.serializers.doc import DocSerializer


# class APIView(ViewSet):

    # def cloudinary(self, request, pk):

    #     response = requests.get(
    #         f'https://api.cloudinary.com/v1_1/${keys.cloudinary}/image/upload').json()

    #     return Response(None, status=status.HTTP_200_OK)


# export const fetchLatandLong = (street, city, state) => {
#     let url = street + ' ' + city + ' ' + state
#     let encode = encodeURIComponent(url)
#     let API = `https://api.myptv.com/geocoding/v1/locations/by-text?searchText=${encode}&apiKey=${keys.ptv}`
#     return fetch(`${API}`)
#         .then(response => response.json())
# }

# export const fetchCloudinary = (formData) => {
#     let API = `https://api.cloudinary.com/v1_1/${keys.cloudinary}/image/upload`
#     return fetch(`${API}`, {
#         method: "POST",
#         body: formData
#     })
#         .then(response => response.json())
# }

# export const getCoffeeShops = (lat, long) => {
#     let API = `https://cors-anywhere.herokuapp.com/https://api.yelp.com/v3/businesses/search?&categories=coffee&open_now=true&limit=7&latitude=${lat}&longitude=${long}`
#     let key = `${keys.yelp}`
#     return fetch(`${API}`, {
#         headers: {
#             Authorization: `Bearer ${key}`,
#             Origin: `localhost`,
#             withCredentials: true,
#         }
#     })
#         .then(response => response.json())
# }
