from django.contrib.auth.models import Group


def get_queryset_for_owner(user, queryset):
    """
    Выборка списка объектов только для их владельцев
    """
    try:
        if user.is_superuser or user.groups.get(name="Moderators"):
            return queryset.order_by("id")
    except Group.DoesNotExist:
        return queryset.filter(owner=user).order_by("id")
