from django.db import models
class Accaunt(models.Model):
    title = models.CharField("Название колледжа", max_length=255)
    login = models.CharField("Логин", max_length=100)
    password = models.CharField("Пароль", max_length=100)
    def __str__(self):
        return f"{self.title} - {self.login} - {self.password}"
# Create your models here.
