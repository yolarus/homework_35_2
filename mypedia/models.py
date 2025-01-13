from django.contrib.auth import get_user_model
from django.db import models

PAYMENT_METHODS = [("cash", "Наличные"),
                   ("transfer_to_account", "Перевод на счет")]


# Create your models here.
class Course(models.Model):
    """
    Модель курса уроков
    """
    name = models.CharField(max_length=150, verbose_name="Название")
    preview = models.ImageField(upload_to="mypedia/courses/previews/", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.SET_NULL,
                              verbose_name="Владелец",
                              null=True,
                              blank=True,
                              related_name="courses")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self):
        return self.name


class Lesson(models.Model):
    """
    Модель урока
    """
    name = models.CharField(max_length=150, verbose_name="Название")
    preview = models.ImageField(upload_to="mypedia/courses/previews/", blank=True, null=True)
    description = models.TextField(verbose_name="Описание", blank=True, null=True)
    video_link = models.TextField(verbose_name="Ссылка на видео", blank=True, null=True)
    course = models.ForeignKey(Course,
                               on_delete=models.PROTECT,
                               verbose_name="Курс",
                               null=True,
                               blank=True,
                               related_name="lessons")
    owner = models.ForeignKey(get_user_model(),
                              on_delete=models.SET_NULL,
                              verbose_name="Владелец",
                              null=True,
                              blank=True,
                              related_name="lessons")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self):
        return self.name


class Payment(models.Model):
    """
    Модель платежей сервиса
    """
    amount = models.FloatField(verbose_name="Сумма оплаты")
    payment_method = models.CharField(max_length=25, choices=PAYMENT_METHODS, verbose_name="Способ оплаты")
    payment_date = models.DateField(auto_now_add=True, verbose_name="Дата платежа")

    owner = models.ForeignKey(get_user_model(),
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
