from time import sleep

from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ToDo
from .serializers import ToDoListSerializer


class ToDoListView(APIView):
    def get(self, *args, **kwargs):
        queryset = ToDo.objects.all()
        serializer = ToDoListSerializer(queryset, many=True)
        return Response(serializer.data)
