from django.db import models


class Role(models.Model):
    name = models.CharField(primary_key=True, max_length=10)

    def __str__(self):
        return self.name


class Department(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class AllocationType(models.Model):
    name = models.CharField(primary_key=True, max_length=20)

    def __str__(self):
        return self.name


class DepartmentGoals(models.Model):
    name = models.CharField(max_length=300)
    value = models.IntegerField(null=True)
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING)
    startDate = models.DateField(auto_now_add=True, null=True)
    endDate = models.DateField(null=True)
    number_of_employee = models.SmallIntegerField(null=True)
    allocation_type = models.ForeignKey(AllocationType, on_delete=models.DO_NOTHING)
    totalUserContribution = models.IntegerField(null=True)


    def __str__(self):
        return self.name


# class UserAllocation(models.Model):
#     type = models.ForeignKey(AllocationType, on_delete=models.DO_NOTHING)
#     departmentGoalsId = models.ForeignKey(DepartmentGoals, on_delete=models.DO_NOTHING)
#     userId = models.ForeignKey('account.Account', on_delete=models.DO_NOTHING)
#
#     def __str__(self):
#         return self.name


class Progress(models.Model):
    employeeInput = models.SmallIntegerField(default=0)
    inputDate = models.DateField(auto_now_add=True)
    individualValue = models.SmallIntegerField(default=0)
    departmentGoalsId = models.ForeignKey(DepartmentGoals, on_delete=models.DO_NOTHING)
    userId = models.ForeignKey('account.Account', on_delete=models.DO_NOTHING)
    departmentGoalName = models.CharField(max_length=300, null=True)
    endDate = models.DateField(null=True)

    def __str__(self):
        return self.individualValue
