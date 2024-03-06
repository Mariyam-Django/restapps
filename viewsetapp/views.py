from rest_framework import viewsets
from .serializer import EmployeeSerializer
from .models import EmployeeModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated



class EmployeeSet(viewsets.ModelViewSet):

    queryset = EmployeeModel.objects.all()
    serializer_class = EmployeeSerializer


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, GeeksforGeeks'}
        return Response(content)


    # Create your views here.
