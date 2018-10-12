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


class AdminExtraManagers(models.Model):
    items = AdminManager()

    class Meta:
        abstract = True


# Mixin 기법?
class UtilMixin(models.Model):
    class Meta:
        abstract = True

    @classmethod
    def show_items(cls):
        # 공통을 사용하기위해 사용
        # cls.__name__ 은 Admin이 되거나 NormalUser 중 하나로 사용
        print(f'- Model({cls.__name__}) items -')
        for item in cls._default_manager.all():
            print(item)

    def set_name(self, new_name):
        ori_name = self.name
        self.name = new_name
        self.save()
        print("{class_name} instance name change ({ori}, {new})".format(
            class_name=self.__class__.__name__,
            ori = ori_name,
            new = new_name
        ))


class NormalUser(UtilMixin, User1):
    # 프록시는 클래스 속성이 있는 여러 모델을 상속할 수 없지만 ( 단 하나의 필드가 있는 모델을 상속받을 수 있다 )
    # 클래스 속성이 없는 여러개의 추상 클래스 모델을 상속받을 수 있다.
    items = NormalUserManager()
    class Meta:
        proxy = True


# 왼쪽에서부터 default_manager 를 넣게된다. 즉, User1 에서 _default_manager를 바꾸고
# 그 후는 신경쓰지 않는다. 즉, 현재는 User1에 _default_Manager가 들어가있고
# User1과 AdminExtraManager의 위치를 바꾸게 되면
# _default_manager에 AdminExtraManagers의 Manager를 갖게된다.
class Admin(UtilMixin, User1, AdminExtraManagers):

    # objects = AdminManager()

    class Meta:
        proxy = True

    def delete_user(self, user):
        user.delete()