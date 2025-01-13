from rest_framework import serializers

from .models import Payment, User


class PaymentSerializer(serializers.ModelSerializer):
    """
    Сериализатор для списка объектов модели Payment
    """
    class Meta:
        model = Payment
        fields = "__all__"


class UserSerializer(serializers.ModelSerializer):
    """
    Сериализатор для модели User
    """

    class Meta:
        model = User
        fields = ["email", "password", "username", "first_name", "last_name", "phone_number", "country", "avatar"]


class UserDetailSerializer(serializers.ModelSerializer):
    """
    Сериализатор для детальной информации об объекте модели User
    """

    payments_history = PaymentSerializer(source="payments", many=True)

    class Meta:
        model = User
        fields = ["email", "password", "username", "first_name", "last_name", "phone_number",
                  "country", "avatar", "payments_history"]
