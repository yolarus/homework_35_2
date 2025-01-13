from rest_framework import serializers

from .models import Course, Lesson, Payment


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
    course_lessons = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = "__all__"

    def get_lessons_count(self, obj):
        """
        Подсчет количества уроков в курсе
        """
        return Lesson.objects.filter(course=obj).count()

    def get_course_lessons(self, obj):
        """
        Список уроков в курсе
        """
        return [lesson.id for lesson in Lesson.objects.filter(course=obj)]


class StaffCourseSerializer(CourseSerializer):
    """
    Сериализатор для модели Course, отображающийся модератору и админу
    """
    lessons_count = serializers.SerializerMethodField()
    course_lessons = LessonSerializer(source="lessons", many=True, read_only=True)


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка объектов модели Payment
    """
    class Meta:
        model = Payment
        fields = "__all__"
