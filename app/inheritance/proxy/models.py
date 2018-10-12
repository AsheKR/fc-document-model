from django.db import models


class User1Manager(models.Manager):
    def normal_users(self):
        # super().get_queryset()
        #   상위 클래스에서 정의한 '기본적으로' 돌려줄 QuerySet
        return super().get_queryset().filter(is_admin=False)
        # return User1.objects.filter(is_admin=False)

    def admin_users(self):
        return super().get_queryset().filter(is_admin=True)
        # return User1.objects.filter(is_admin=True)


class User1(models.Model):
    # 가능항 메서드
    # - 유저 삭제
    # - 유저 이름 바꾸기
    # - 유저를 관리자로 만들기
    name = models.CharField('이름', max_length=40)
    is_admin = models.BooleanField('관리자', blank=True)

    # 이 클래스에 커스텀 매니저를 적용
    objects = User1Manager()

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '유저'
        verbose_name_plural = '유저목록'

    def find_user(self, name):
        return User1.objects.get(name__contains=name)


class NormalUserManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=False)


class AdminManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class NormalUser(User1):
    objects = NormalUserManager()
    class Meta:
        proxy = True


class Admin(User1):
    objects = AdminManager()
    class Meta:
        proxy = True

    def delete_user(self, user):
        user.delete()