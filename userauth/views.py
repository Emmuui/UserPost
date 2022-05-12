from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from userauth import models
from userauth.api.serializers import ProfileUserSerializer, PublicationListSerializer, FollowerSerializer
from rest_framework import viewsets, generics
from rest_framework.response import Response

from .tasks import send_email_to_all_user


class UserViewSet(viewsets.ViewSet):

    def list(self, request):
        queryset = models.ProfileUser.objects.all()
        serializer = ProfileUserSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = models.ProfileUser.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = ProfileUserSerializer(user)
        return Response(serializer.data)


class PublicationView(generics.ListAPIView):

    queryset = models.Publication.objects.all()
    serializer_class = PublicationListSerializer


class FollowerView(generics.ListAPIView):

    queryset = models.Follower.objects.all()
    serializer_class = FollowerSerializer


def send_email_to_all_user_view(request):
    send_email_to_all_user.delay()
    return HttpResponse('Test')
