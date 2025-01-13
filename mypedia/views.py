from rest_framework import generics, viewsets

from .models import Course, Lesson
from .serializers import CourseSerializer, LessonSerializer


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """
    Вьюсет для CRUD операций с моделью Course
    """
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class LessonListCreateAPIView(generics.ListCreateAPIView):
    """
    Дженерик для отображения списка и создания нового объекта Lesson:
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer


class LessonRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Дженерик для просмотра, редактирования и удаления объекта Lesson:
    """
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
