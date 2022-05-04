from django.urls import path
from . import views

urlpatterns = [
    path('create-department-goals/', views.DepartmentGoalCreate.as_view(), name='create-department-goals'),
    path('create-progress/', views.ProgressCreate.as_view(), name='create-progress'),
    path('update-progress/<str:pk>/', views.ProgressUpdate.as_view(), name='update-progress'),
    path('update-user-input/<str:fk>/', views.UpdateTotalUserContribution.as_view(), name='update-user-input'),
    path('get-department-goals/<str:fk>/', views.FindDepartmentGoals.as_view(), name='get-department-goals'),
    path('update-progress/<str:fk>/<str:fk2>/', views.UpdateProgress.as_view(), name='update-progress'),
    path('get-progress/<str:fk>/<str:fk2>/', views.GetProgressByUserIdDepartmentGoalsId.as_view(), name='get-progress'),
    path('get-progress/<str:fk>/', views.FindProgressByDepartmentGoal.as_view(), name='get-progress'),
    path('get-progress-by-userid/<str:fk>/', views.FindProgressOfUser.as_view(), name='get-progress-By-userid')
]