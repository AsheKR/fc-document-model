from django.db import models


class Place1(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=80, blank=True)

    def __str__(self):
        return f'{self.name} [Place]'

    class Meta:
        # 이 이름을 작성하면 클래스 명을 바꾸어도 DB에는 아무 변화가 일어나지 않는다.
        # 또한 makemigrations 시 오류가 발생한다. ORM이 인식하지 못하기 때문.
        db_table = 'Inheritance_MultiTable_Place'


def get_removed_place():
    # 한줄로 줄여쓸 수 있음
    # return Place1.objects.get_or_create(name='철거됨')[0]
    try:
        Place1.objects.get(name="철거됨")
    except Place1.DoesNotExist:
        place = Place1.objects.create(name='철거됨')
    return place

class Restaurant1(Place1):
    # MultiTable inheritance  구현시 암시적으로 생성되는 OTO Field
    # <부모클래스의 소문자화>_ptr = models.OneToOneField(<부모클래스>)
    # place1_ptr = modelss.OneToOneField(Place1)
    # -> 임의의 필드에 parent_link=True 옵션을 주면 <부모클래스의 소문자화>_ptr 필드가 생성되지 않음
    place_ptr = models.OneToOneField(
        Place1,
        parent_link=True,
        primary_key=True,
        on_delete=models.CASCADE
    )
    serves_hot_dogs = models.BooleanField(default=False)
    serves_pizza = models.BooleanField(default=False)

    old_place = models.ForeignKey(
        Place1, verbose_name='이전 가게가 있던 장소',
        # 이전 가게가 있던 건물이 없어질 경우
        # (해당 장소 또는 건물이 없어졌음) 이라는 정보를 담자
        #   -> 위와같은 정보를 담고 있는 Place1 (DB row)가 필요함
        on_delete=models.SET(get_removed_place),
        related_name='old_restaurants',
        blank=True, null=True,
    )

    def __str__(self):
        return f'{self.name} [Restaurant]'

    class Meta:
        db_table = 'Inheritance_MultiTable_Restaurant'
