from django.db import models

__all__ = (
    'FacebookUser',
)


class FacebookUser(models.Model):
    name = models.CharField(max_length=30)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # 이한영 (친구: a, b, c)
        # QuerySet 순회 및 문자열 포매팅
        return self.name+' (친구: '+','.join([x.name for x in self.friends.all()])+')'

    def __repr__(self):
        # 이한영 (친구: a, b, c)
        # QuerySet 순회 및 문자열 포매팅
        return self.name+' (친구: '+','.join(self.friends.values_list('name', flat=True))+')'
