from django.db import models

class TimestampFields(models.Model):
    """
    Абстрактная модель для добавления полей даты создания и обновления.
    """
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    class Meta:
        # Это ключевой момент! Эта модель не будет создана в базе данных.
        abstract = True


class Project(TimestampFields):
    """Объект на котором проводят измерения."""

    name = models.CharField(max_length=100, verbose_name='Название')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'
        

    def __str__(self):
        return f"{self.name} ({self.latitude}, {self.longitude})"


class Measurement(models.Model):
    """Измерение температуры на объекте."""

    value = models.FloatField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )
    image = models.ImageField(
        upload_to='measurement_images/',
        null=True,
        blank=True,
        default=None,
        verbose_name='Снимок'
    )


    def __str__(self):
        return f"{self.value} ({self.project.name})"
