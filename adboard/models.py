from django.db import models

class Adb(models.Model):
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    content = models.TextField(null=True, blank=True, verbose_name='Описание')
    published = models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Опубликовано')
    tag = models.ForeignKey('Tag', null=True, on_delete=models.PROTECT, verbose_name='Тег')

    class Meta:
        verbose_name_plural = 'Заметки'
        verbose_name = 'Заметка'
        ordering = ['-published']

class Tag(models.Model):
    name = models.CharField(max_length=20, db_index=True, verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Теги'
        verbose_name = 'Тег'
        ordering = ['name']