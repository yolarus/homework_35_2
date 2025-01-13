from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser
from .models import Payment, User
from .serializers import PaymentSerializer, UserDetailSerializer, UserSerializer
from .permissions import IsModerator


# Create your views here.
class UserListCreateAPIView(generics.ListCreateAPIView):
    """
    Дженерик для отображения списка и создания нового объекта User:
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_permissions(self):
        """
        Проверка разрешений в зависимости от HTTP-запроса
        """
        if self.request.method == "POST":
            self.permission_classes = [AllowAny]
        elif self.request.method == "GET":
            self.permission_classes = [IsModerator | IsAdminUser]
        return super().get_permissions()

    def perform_create(self, serializer):
        """
        Сохранение пароля и активация учетной записи при создании
        """
        user = serializer.save(is_active=True)
        user.set_password(user.password)
        user.save()


class UserRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Дженерик для просмотра, редактирования и удаления объекта User:
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer


class PaymentListCreateAPIView(generics.ListCreateAPIView):
    """
    Дженерик для отображения списка и создания нового объекта Payment:
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    ordering_fields = ["payment_date"]
    filterset_fields = ["course", "lesson", "payment_method"]


class PaymentRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    """
    Дженерик для просмотра, редактирования и удаления объекта Payment:
    """
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
