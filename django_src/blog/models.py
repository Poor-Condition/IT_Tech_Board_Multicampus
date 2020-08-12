from django.db import models

class News(models.Model):
    objects = None
    news_title = models.CharField(db_column="제목", max_length=400)
    news_url = models.URLField(db_column="링크", max_length=400)
    image_link = models.CharField(db_column="이미지", max_length=400)
    published_date = models.CharField(db_column="등록날짜", max_length=400)

    class Meta:
        managed = False
        db_table = "article_new_tech"

    def __str__(self):
        return self.news_title