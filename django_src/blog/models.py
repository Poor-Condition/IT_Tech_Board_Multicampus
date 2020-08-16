from django.db import models

class News_dev(models.Model):
    objects = None
    news_title = models.CharField(db_column="제목", max_length=400)
    news_url = models.URLField(db_column="링크", max_length=400)
    image_link = models.CharField(db_column="이미지", max_length=400)
    published_date = models.CharField(db_column="등록날짜", max_length=400)

    class Meta:
        managed = False
        db_table = "articles"

    def __str__(self):
        return self.news_title

class Articles(models.Model):
    objects = None
    news_title = models.CharField(db_column="제목", max_length=400)
    news_url = models.URLField(db_column="링크", max_length=400)
    image_link = models.CharField(db_column="이미지", max_length=400)
    published_date = models.CharField(db_column="등록날짜", max_length=400)
    field = models.CharField(db_column="분류", max_length=50)

    class Meta:
        managed = False
        db_table = "articles"

    def __str__(self):
        return self.news_title

class News_cloud(models.Model):
    objects = None
    news_title = models.CharField(db_column="제목", max_length=400)
    news_url = models.URLField(db_column="링크", max_length=400)
    image_link = models.CharField(db_column="이미지", max_length=400)
    published_date = models.CharField(db_column="등록날짜", max_length=400)

    class Meta:
        managed = False
        db_table = "article_cloud"

    def __str__(self):
        return self.news_title

class News_new_tech(models.Model):
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



class Jobs_Cloud(models.Model):
    objects = None

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
        db_table = "job_list"

    def __str__(self):
        return self.job_title

class Jobs_Python(models.Model):
    objects = None

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
        db_table = "job_python"

    def __str__(self):
        return self.job_title

class Jobs_DB(models.Model):
    objects = None

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
        db_table = "job_list"

    def __str__(self):
        return self.job_title


class Contest_game(models.Model):
    objects=None
    #'공모이름', '이미지', '분야', '응모대상', '주최/주관', '후원/협찬', '접수기간', '총 상금', '1등 상금', '홈페이지', '첨부파일'
    contest_title=models.CharField(db_column="공모이름", max_length=400)
    contest_image = models.CharField(db_column="이미지", max_length=400)
    contest_category = models.CharField(db_column="분야", max_length=400)
    contest_participant = models.CharField(db_column="응모대상", max_length=400)
    contest_organizer = models.CharField(db_column="주최/주관", max_length=400)
    contest_sponsor = models.CharField(db_column="후원/협찬", max_length=400)
    contest_period = models.CharField(db_column="접수기간", max_length=400)
    contest_money = models.CharField(db_column="총 상금", max_length=400)
    contest_firstmoney = models.CharField(db_column="1등 상금", max_length=400)
    contest_homepage = models.CharField(db_column="홈페이지", max_length=400)
    contest_file = models.CharField(db_column="첨부파일", max_length=400)

    class Meta:
        managed = False
        db_table = "contest_game"

    def __str__(self):
        return self.contest_title

class Contest_science(models.Model):
    objects=None
    #'공모이름', '이미지', '분야', '응모대상', '주최/주관', '후원/협찬', '접수기간', '총 상금', '1등 상금', '홈페이지', '첨부파일'
    contest_title = models.CharField(db_column="공모이름", max_length=400)
    contest_image = models.CharField(db_column="이미지", max_length=400)
    contest_category = models.CharField(db_column="분야", max_length=400)
    contest_participant = models.CharField(db_column="응모대상", max_length=400)
    contest_organizer = models.CharField(db_column="주최/주관", max_length=400)
    contest_sponsor = models.CharField(db_column="후원/협찬", max_length=400)
    contest_period = models.CharField(db_column="접수기간", max_length=400)
    contest_money = models.CharField(db_column="총 상금", max_length=400)
    contest_firstmoney = models.CharField(db_column="1등 상금", max_length=400)
    contest_homepage = models.CharField(db_column="홈페이지", max_length=400)
    contest_file = models.CharField(db_column="첨부파일", max_length=400)

    class Meta:
        managed = False
        db_table = "contest_science"

    def __str__(self):
        return self.contest_title


class Contest_job(models.Model):
    objects=None
    #'공모이름', '이미지', '분야', '응모대상', '주최/주관', '후원/협찬', '접수기간', '총 상금', '1등 상금', '홈페이지', '첨부파일'
    contest_title = models.CharField(db_column="공모이름", max_length=400)
    contest_image = models.CharField(db_column="이미지", max_length=400)
    contest_category = models.CharField(db_column="분야", max_length=400)
    contest_participant = models.CharField(db_column="응모대상", max_length=400)
    contest_organizer = models.CharField(db_column="주최/주관", max_length=400)
    contest_sponsor = models.CharField(db_column="후원/협찬", max_length=400)
    contest_period = models.CharField(db_column="접수기간", max_length=400)
    contest_money = models.CharField(db_column="총 상금", max_length=400)
    contest_firstmoney = models.CharField(db_column="1등 상금", max_length=400)
    contest_homepage = models.CharField(db_column="홈페이지", max_length=400)
    contest_file = models.CharField(db_column="첨부파일", max_length=400)

    class Meta:
        managed = False
        db_table = "contest_job"

    def __str__(self):
        return self.contest_title