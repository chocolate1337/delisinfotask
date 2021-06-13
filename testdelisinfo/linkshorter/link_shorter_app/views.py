from django.http import Http404
from django.shortcuts import render

from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Link
from .serializers import LinkSerializer


class LinkAPIView(APIView):

    permission_classes = [AllowAny]
    serializer_class = LinkSerializer

    def get_object(self, pk):
        try:
            return Link.objects.get(pk=pk)
        except Link.DoesNotExist:
            raise Http404


    def post(self, request):

        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(
            {
                'short_url': serializer.data.get('short_url', None),
            },
            status=status.HTTP_201_CREATED,
        )

    def get(self, request):

        link = Link.objects.all()
        serializer = LinkSerializer(link, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
