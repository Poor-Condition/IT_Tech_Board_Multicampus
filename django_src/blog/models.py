from django.db import models

# Create your models here.
class News(models.Model):
    news_id = models.AutoField(db_column="id")
    news_title = models.CharField(db_column="제목", max_length=400)
    news_url = models.URLField(db_column="링크", max_length=400)
    image_link = models.CharField(db_column="이미지", max_length=400)
    published_date = models.DateTimeField(db_column="등록날짜", blank=True, null=True)

    class Meta:
        managed = True
        db_table = "article_cloud"