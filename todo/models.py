from django.db import models


class ToDo(models.Model):
    class ToDoStatus:
        NEW = "new"
        DOING = "doing"
        IN_QA = "in_qa"
        DONE = "done"

        def choices(self) -> list[tuple[str, str]]:
            return [
                (self.NEW, "Yangi"),
                (self.DOING, "Bajarilmoqda"),
                (self.IN_QA, "Tekshirilmoqda"),
                (self.DONE, "Yakunlandi"),
            ]

    name = models.CharField(max_length=255)
    comment = models.TextField(default="")
    status = models.CharField(max_length=50, choices=ToDoStatus().choices(), default=ToDoStatus.NEW)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return self.name