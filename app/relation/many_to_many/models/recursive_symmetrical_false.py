from django.db import models

__all__ = (
    'InstagramUser',
)


class InstagramUser(models.Model):
    # 다른사람이 자신을 follow하는 사람 목록
    # - followers
    #   팔로워목록
    # 자신이 다른사람을 follow한 사람 목록
    # - following
    #   팔로우목록
    # A, B
    # A가 B를 팔로우한 경우
    # - A는 B의 follower (팔로워)
    # - B는 A의 follweree (팔로우)

    name = models.CharField(max_length=50)
    # 내가 follow를 한 유저 목록
    following = models.ManyToManyField(
        'self',
        # 하나가 추가될때 다른쪽은 추가되지 않게
        symmetrical=False,
        # 역 참조할 때 사용되는 인자
        related_name='followers',
    )

    def __str__(self):
        return self.name
