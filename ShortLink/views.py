from rest_framework.views import APIView
from rest_framework.response import Response
from .models import ShortLink
from rest_framework import status
import random
import string
from django.shortcuts import get_object_or_404
from django.http import HttpResponseRedirect
from .serializers import ShortLinkSerializers

# Create your views here.

class ShortLinkCreateView(APIView):
    def generate_short_code(self, length=6):
        characters = string.ascii_letters + string.digits
        return ''.join(random.choice(characters) for _ in range(length))
    
    def post(self, request):
        long_url = request.data.get('long_url')
        if not long_url:
            return Response({'error':'Long Url is required.'}, status=status.HTTP_400_BAD_REQUEST)
        
        short_code = self.generate_short_code()
        short_link = "http://localhost:8000/" + short_code
        serialize = ShortLink(short_code=short_code, long_url=long_url)
        serialize.save()
        print(short_link)

        return Response({'short_url': short_link}, status=status.HTTP_201_CREATED)
    
    def get(self, request):
        short_urls = ShortLink.objects.all()
        serializer = ShortLinkSerializers(short_urls, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class ShortLinkURLView(APIView):

    def get(self, request, short_code):
        try:
            shortcode = ShortLink.objects.get(short_code=short_code)
        except ShortLink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShortLinkSerializers(shortcode)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, short_code):
        shortcode = ShortLink.objects.get(short_code=short_code)
        shortcode.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class RedirectShortURL(APIView):
    def get(self, request, short_code):
        url_mapping = get_object_or_404(ShortLink, short_code=short_code)
        print(url_mapping)
        return HttpResponseRedirect(url_mapping.long_url)