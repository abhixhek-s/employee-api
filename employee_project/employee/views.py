from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Employee
from .serializers import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):

        return Response({
            "type": str(type(request.data)),
            "is_list": isinstance(request.data, list),
            "data": request.data
        })