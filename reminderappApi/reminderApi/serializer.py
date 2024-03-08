from rest_framework import serializers
from reminderApi.models import ReminderInfo

class ReminderSerializer(serializers.ModelSerializer):

    class Meta:
        model = ReminderInfo
        fields = "__all__"