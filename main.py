import os

from django.core.management import execute_from_command_line


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project.settings")
execute_from_command_line("manage.py runserver 0.0.0.0:8000".split())


# код с предыдущих шагов
# print("Всего пропусков:", Passcard.objects.count())  # noqa: T001
# print("Активных пропусков (фильтр app):", len([passcard for passcard in Passcard.objects.all() if passcard.is_active]))
# print("Активных пропусков (фильтр бд):", Passcard.objects.filter(is_active=True).count())  # noqa: T001
