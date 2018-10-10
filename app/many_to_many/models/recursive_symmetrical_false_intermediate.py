from django.db import models

__all__ = (
    'TwitterUser',
)


class TwitterUser(models.Model):
    """
    특정 유저가 다른 유저를 (인스턴스 메서드)
        follow (팔로우하기)
        block  (차단하기)



    중간 모델이 저장하는 정보
        from_user
            어떤 유저가 '만든' 관계인지
        to_user
            관계의 '대상'이 되는 유저
        relation_type
            follow 또는 block (팔로우 또는 차단)


    용어 정리
        - 다른사람이 자신을 follow하는 사람 목록
            followers (팔로워목록)

        - 자신이 다른사람을 follow한 사람 목록
            following (팔로우목록)

        - 자신이 다른사람을 block 한 목록
            block_list

        A, B
        - A가 B를 팔로우한 경우
            A는 B의 follower (팔로워)
            B는 A의 follweree (팔로우)
    """
    name = models.CharField(max_length=50)
    relation_users = models.ManyToManyField(
        'self',
        through='Relation',
        symmetrical=False,
    )

    def __str__(self):
        return self.name


class Relation(models.Model):
    CHOICES_RELATION_TYPE = (
        ('f', 'Follow'),
        ('b', 'Block'),
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_from_user',
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        related_name='relations_by_to_user',
    )
    relation_type = models.CharField(
        choices=CHOICES_RELATION_TYPE,
        max_length=1,
    )
    created_at = models.DateTimeField(auto_now_add=True)
