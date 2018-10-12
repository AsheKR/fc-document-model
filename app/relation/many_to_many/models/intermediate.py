from django.db import models

_all__ = (
    'Person',
    'Group',
    'Membership'
)


class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    # related_name
    # 매니저 객체로 접근할 때 사용하는 이름
    # 기본형태 : 클래스명 소문자_set
    #
    # related_query_name
    # Filter 같은 것으로 사용하는 이름
    # 기본형태 : 클래스명의 소문자
    # .filter(키=값)
    #   에서 '키'에 다른 특정 테이블을 가리키고 싶을 때
    #   MTM 필드를 정의한 테이블의 경우는 해당 필드명을 사용
    #           Group의 경우에 해당 -> 'members'로 Person의 내용을 필터링 가능
    #   MTM 필드의 target 테이블의 경우에는 필드가 정의되어있지 않고,
    #       이때 사용하는 이름이 related_query_name 속성에 할당된 이름
    #           Person의 경우 해당 -> 자동 생성된 기본이름 'group'으로 Group의 내용 필터링 가능
    #

    def __str__(self):
        return self.name


class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateField()
    invite_reason = models.CharField(max_length=64)