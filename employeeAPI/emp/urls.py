from django.urls import path
from . views import EmployeeCreateApi,EmployeeUpdateApi,EmployeeDeleteApi,EmployeeApi
urlpatterns = [
    path('api/', EmployeeCreateApi.as_view()),
    path('update/<int:pk>/',EmployeeUpdateApi.as_view()),
    path('delete/<int:pk>/',EmployeeDeleteApi.as_view()),
    path('emp/',EmployeeApi.as_view())
]
