import os
import requests
from rest_framework import status
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.mixins import UpdateModelMixin
from rest_framework.permissions import IsAdminUser
from apps.dashboard.models import Dashboard
from apps.dashboard.serializers import DashboardSerializer


class DashboardView(ListCreateAPIView, UpdateModelMixin):
    permission_classes = [IsAdminUser]
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.order_by('-score', '-stage')[:5]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            previous_score = Dashboard.objects.get(nickname=request.data['nickname'])
            if previous_score.score >= int(request.data['score']):
                return Response(
                    status=status.HTTP_200_OK,
                    data={
                        'updated': False,
                        'data': self.serializer_class(previous_score).data
                    }
                )
            else:
                self.perform_update(serializer)
        except Dashboard.DoesNotExist:
            self.perform_create(serializer)

        return Response(
            status=status.HTTP_201_CREATED,
            data={
                'updated': True,
                'data': serializer.data
            }
        )

    # def get(self, request, *args, **kwargs):
    #    url = os.environ('PROXY_SERVER_URL')
    #    response = requests.get(url).json()
    #    print(response)
    #    return Response(response)

    # def post(self, request, *args, **kwargs):
    #    serializer = self.get_serializer(data=request.data)
    #    serializer.is_valid(raise_exception=True)
    #
    #    url = os.environ('PROXY_SERVER_URL')
    #    response = requests.post(url, json=serializer.data).json()
    #    return Response(response)
