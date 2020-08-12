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


class Jobs(models.Model):
    company = models.CharField(db_column='기업명', max_length=100)
    job_title = models.CharField(db_column='직무', max_length=300)
    experience = models.CharField(db_column='경력사항', max_length=300)
    edu_level = models.CharField(db_column='학력', max_length=50)
    type = models.CharField(db_column='근무형태', max_length=50)
    location = models.CharField(db_column='근무지', max_length=50)
    category = models.CharField(db_column='분류', max_length=300)
    link = models.CharField(db_column='상세링크', max_length=300)

    class Meta:
        managed = False
        db_table = "jobs_cloud"

    def __str__(self):
        return self.job_title