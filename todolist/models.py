from django.db import models


class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name='Задача')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    done = models.BooleanField(db_index=True, default=False, verbose_name='Сделано')
    done_time = models.DateTimeField(null=True, blank=True, verbose_name='Когда сделано')

    class Meta:
        verbose_name_plural = 'Задачи'
        verbose_name = 'Задача'
        ordering = ['-done', '-published']

    def __str__(self):
        return self.name
