from django.urls import path
from .views import StudentCreateApi,StudentUpdateApi,StudentDeleteApi,StudentApi
urlpatterns = [
    path('create/',StudentCreateApi.as_view()),
    path('update/<int:pk>/',StudentUpdateApi.as_view()),
    path('delete/<int:pk>/',StudentDeleteApi.as_view()),
    path('api/',StudentApi.as_view()),
]
