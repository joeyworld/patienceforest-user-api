from rest_framework.serializers import ModelSerializer
from apps.dashboard.models import Dashboard


class DashboardSerializer(ModelSerializer):
    class Meta:
        model = Dashboard
        exclude = ['id']
