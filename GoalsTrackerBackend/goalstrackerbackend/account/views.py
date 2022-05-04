from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import AccountSerializer
from .models import Account


class AccountCreate(APIView):
    def put(self, request):
        serializer = AccountSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response('Error with creating')


class FindOutDepartment(APIView):
    def get(self, request, fk):
        department = Account.objects.filter(department_id=fk).filter(role_id="Employee")
        serializer = AccountSerializer(department, many=True)

        return Response(serializer.data)


class FindUserByUserId(APIView):
    def get(self, request, pk):
        department = Account.objects.get(id=pk)
        serializer = AccountSerializer(department, many=False)

        return Response(serializer.data)
