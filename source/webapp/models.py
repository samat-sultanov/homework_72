from django.db import models

CHOICES = [('new', 'Новая'), ('moderated', 'Модерированная')]


class Phrase(models.Model):
    text = models.TextField(max_length=500, verbose_name='Текст')
    author = models.CharField(max_length=100, verbose_name='Автор')
    email = models.EmailField(max_length=70, unique=True, verbose_name='Почта')
    rating = models.IntegerField(default=0, verbose_name='Рейтинг')
    status = models.CharField(max_length=50, default='new', choices=CHOICES, verbose_name='Статус')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата-время добавления')

    class Meta:
        permissions = [("view_new_phrases", "Видеть новые цитаты")]

    def __str__(self):
        return f'{self.pk}: {self.author} - {self.text}'
