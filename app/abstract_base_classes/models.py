from django.db import models

# 1. AbstractBaseClasses
#   자식 테이블만 존재
# 2. Multi table inheritance
#   부모, 자식 테이블이 모두 존재
# 3. Proxy 모델
# 부모 테이블만 존재


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)