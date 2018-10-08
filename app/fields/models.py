from django.db import models


# Create your models here.
class Persons(models.Model):
    SHIRT_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
    )
    name = models.CharField('이름', max_length=60)
    shirt_size = models.CharField(
        max_length=1,
        choices=SHIRT_SIZES,
        help_text='S,M,L 중에 선택',
    )

    # # 폼 검증에 사용하는 것이 blank
    # # 그러므로 폼에서 빈 값을 넣고 SUBMIT 했을 경우 폼은 인정해주지만 DB에서 오류가 발생한다.
    # age1 = models.IntegerField(blank=True)
    # # DB에 빈 값을 허용하는것
    # # 하지만 폼에서는 빈 값을 허용하지 않는다.
    # age2 = models.IntegerField(null=True)
    # # 두개를 같이 쓰면 폼에서도 허용하고, DB에서도 허용하게 된다.

    age = models.IntegerField(blank=True, null=True)
    stars = models.IntegerField(default=0)
    nickname = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True,
    )