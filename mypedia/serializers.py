from rest_framework import serializers

from .models import Course, Lesson


class LessonSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Lesson
    """
    class Meta:
        model = Lesson
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели Course
    """

    lessons_count = serializers.SerializerMethodField()
    course_lessons = LessonSerializer(source="lessons", many=True)

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, obj):
        """
        Подсчет количества уроков в курсе
        """
        return Lesson.objects.filter(course=obj).count()
