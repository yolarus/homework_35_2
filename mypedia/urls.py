from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .apps import MypediaConfig

app_name = MypediaConfig.name

router = DefaultRouter()
router.register("courses", views.CourseViewSet, basename="courses")

urlpatterns = [
    path("lessons/", views.LessonListCreateAPIView.as_view(), name="lessons"),
    path("lessons/<int:pk>/", views.LessonRetrieveUpdateDestroyAPIView.as_view(), name="lesson"),
] + router.urls
