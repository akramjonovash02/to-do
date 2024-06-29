from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from mainApp.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token-refresh/', TokenRefreshView.as_view()),

    path('mytasks', MyTasksAPIView.as_view()),
    path('tasks/<int:pk>/', TaskListView.as_view()),
    ]
