import datetime
from django.db import models

from django.utils import timezone

class Article(models.Model):
	article_title = models.CharField('название статьи', max_length = 200) #VarChar в MySQL
	article_text = models.TextField('текст статьи') #Большое текстовое поле
	pub_date = models.DateTimeField('дата публикации')

	def __str__(self):
		return self.article_title

	def was_published_recently(self):#была ли статья опубликована недавно? (7 дней)
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7)) 

	class Meta:
		verbose_name = "Cтатья" #как будет отображаться в админке название этой модели (Article)
		verbose_name_plural = "Статьи"

class Comment(models.Model):
	article = models.ForeignKey(Article, on_delete=models.CASCADE)
	#*все Комментарии будут привязаны к Статьям (экземплярам класса Atricle)
	author_name = models.CharField('автор статьи', max_length = 50)
	comment_text = models.CharField('текст комментария', max_length = 200)

	def __str__(self):
		return self.author_name

	class Meta:
		verbose_name = "Комментарий" #как будет отображаться в админке название этой модели (Comment)
		verbose_name_plural = "Комментарии"