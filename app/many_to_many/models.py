from django.db import models


class Topping(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Pizza(models.Model):
    name = models.CharField(max_length=50)
    # 피자에 토핑이 들어가니까 여기 선
    toppings = models.ManyToManyField(Topping)

    def __str__(self):
        return self.name


class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self')

    def __str__(self):
        return self.name

class Person(models.Model):
    name = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=120)
    """
    MTMField에 두번째 인자를 주지않고 생성하면 자동으로 생성된다.
    하지만 추가적인 필드가 필요할 때 through 키워드를 이용하면 중간 모델을 가리키도록 하여 연결 가능하다.
    """
    # 그룹에 사람이 들어가니까 여기 선언
    members = models.ManyToManyField(Person, through='Membership', through_fields=('group', 'person'))

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    date_joined = models.DateTimeField()
    invite_reason = models.CharField(max_length=64)