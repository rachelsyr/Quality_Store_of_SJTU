from django.db import models
from django.utils import timezone
# Create your models here.


class Comment(models.Model):
    name = models.CharField('名字', max_length=50)
    text = models.TextField('内容')
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    shop = models.ForeignKey('shop.Shop', null=True, verbose_name='店铺', on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])