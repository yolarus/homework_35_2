from django.contrib.auth.models import AbstractUser
from django.db import models

from mypedia.models import Course, Lesson

PAYMENT_METHODS = [("cash", "Наличные"),
                   ("transfer_to_account", "Перевод на счет")]


# Create your models here.
class User(AbstractUser):
    """
    Модель пользователей сервиса
    """
    email = models.EmailField(unique=True, verbose_name="Email")
    username = models.CharField(max_length=25,
                                verbose_name="Ник пользователя",
                                null=True,
                                blank=True)

    phone_number = models.CharField(max_length=15,
                                    verbose_name="Телефон",
                                    null=True,
                                    blank=True)
    avatar = models.ImageField(upload_to="users/avatars/",
                               verbose_name="Аватар",
                               null=True,
                               blank=True)
    country = models.CharField(max_length=100,
                               verbose_name="Страна",
                               null=True,
                               blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email


class Payment(models.Model):
    """
    Модель платежей сервиса
    """
    amount = models.FloatField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=25, choices=PAYMENT_METHODS, verbose_name="Способ оплаты")
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата платежа")

    user = models.ForeignKey(User,
                             on_delete=models.CASCADE,
                             verbose_name="Пользователь",
                             null=True,
                             blank=True,
                             related_name="payments")
    course = models.ForeignKey(Course,
                               on_delete=models.CASCADE,
                               verbose_name="Оплаченный курс",
                               null=True,
                               blank=True,
                               related_name="payments")
    lesson = models.ForeignKey(Lesson,
                               on_delete=models.CASCADE,
                               verbose_name="Оплаченный урок",
                               null=True,
                               blank=True,
                               related_name="payments")

    class Meta:
        verbose_name = "Платеж"
        verbose_name_plural = "Платежи"

    def __str__(self):
        return f"Платеж №{self.pk} от {self.payment_date} - {self.amount} руб."
