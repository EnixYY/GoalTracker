from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import DepartmentGoalsSerializer
from .serializers import ProgressSerializer
from .models import Progress
from .models import DepartmentGoals



class DepartmentGoalCreate(APIView):
    def put(self, request):
        serializer = DepartmentGoalsSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response('Error with creating')


class ProgressCreate(APIView):
    def put(self, request):
        serializer = ProgressSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)
        else:
            return Response('Error with creating')


class ProgressUpdate(APIView):
    def patch(self, request, pk):
        progress = Progress.objects.get(id=pk)
        serializer = ProgressSerializer(instance=progress, data=request.data, partial=True)
        #instance is the original; data is the one you wanna update it to
        #partial = True means you can just update one part of the instance instead of every attribute

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class FindDepartmentGoals(APIView):
    def get(self, request, fk):
        departmentgoals = DepartmentGoals.objects.filter(department_id=fk)
        serializer = DepartmentGoalsSerializer(departmentgoals, many=True)

        return Response(serializer.data)


class UpdateProgress(APIView):
    def patch(self, request, fk, fk2):
        progress = Progress.objects.filter(departmentGoalsId_id=int(fk)).get(userId_id=int(fk2))
        serializer = ProgressSerializer(instance=progress, data=request.data, partial=True)

        if serializer.is_valid():
            serializer.save()

        return Response(serializer.data)


class FindProgressByDepartmentGoal(APIView):
    def get(self, request, fk):
        progress = Progress.objects.filter(departmentGoalsId_id=fk)
        serializer = ProgressSerializer(progress, many=True)

        return Response(serializer.data)


class UpdateTotalUserContribution(APIView):
    def patch(self, request, fk):
        departmentgoals = DepartmentGoals.objects.get(id=fk)
        serializer = DepartmentGoalsSerializer(instance=departmentgoals, data=request.data, partial=True)
        #instance is the original; data is the one you wanna update it to
        #partial = True means you can just update one part of the instance instead of every attribute

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        else:
            return Response('Error with updating')


class FindProgressOfUser(APIView):
    def get(self, request, fk):
        progress = Progress.objects.filter(userId_id=fk)
        serializer = ProgressSerializer(progress, many=True)

        return Response(serializer.data)


class GetProgressByUserIdDepartmentGoalsId(APIView):
    def get(self, request, fk, fk2):
        progress = Progress.objects.filter(departmentGoalsId_id=int(fk)).filter(userId_id=int(fk2))
        serializer = ProgressSerializer(progress, many=True)

        return Response(serializer.data)