from rest_framework import serializers
from .models import DepartmentGoals
from .models import Progress


class DepartmentGoalsSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentGoals
        fields = '__all__'


class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Progress
        fields = '__all__'
