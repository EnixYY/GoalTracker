from django.urls import path
from . import views

urlpatterns = [
    path('create-account/', views.AccountCreate.as_view(), name='create-account'),
    path('get-department/<str:fk>/', views.FindOutDepartment.as_view(), name='get-department'),
    path('get-account/<str:pk>/', views.FindUserByUserId.as_view(), name='get-account')
]
