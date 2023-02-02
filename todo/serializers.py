from datetime import datetime

from rest_framework import serializers

from .models import ToDo


class ToDoListSerializer(serializers.ModelSerializer):
    status = serializers.SerializerMethodField()
    age = serializers.SerializerMethodField()

    class Meta:
        model = ToDo
        fields = "__all__"
    
    def get_status(self, obj):
        return {
            "value": obj.status,
            "readable": obj.get_status_display()
        }
    
    def get_age(self, obj):
        return (datetime.now() - obj.created_at).seconds