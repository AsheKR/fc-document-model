from django.db import models

# 1. AbstractBaseClasses
#   자식 테이블만 존재
# 2. Multi table inheritance
#   부모, 자식 테이블이 모두 존재
# 3. Proxy 모델
# 부모 테이블만 존재

__all__ = (
    'CommonInfo',
    'Student',
)


class CommonInfo(models.Model):
    # DB에 넣을 때 자동으로 정렬
    name = models.CharField(max_length=100, db_index=True)
    age = models.PositiveIntegerField()

    def __str__(self):
        return self.name

    class Meta:
        # 상속하면 FALSE가 된다
        abstract = True
        # 쿼리로 가져올 때 자동으로 정렬
        ordering = ['name']


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)

    class Meta(CommonInfo.Meta):
        # 폼에서 보여줄 내용
        verbose_name = '학생'
        # 여러개일 때는 자동으로 s가 붙어서 이 옵션을 주면 이름을 바꿀 수 있다
        verbose_name_plural = '학생 목록'