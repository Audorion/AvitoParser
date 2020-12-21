import django_tables2 as tables
from .models import UserRequest


class UserRequestTable(tables.Table):
    class Meta:
        row_attrs = {"style": lambda record: "color: #fff;"}
        model = UserRequest
        template_name = "django_tables2/bootstrap.html"
        fields = ("region", "request_words", "date", "counter")
