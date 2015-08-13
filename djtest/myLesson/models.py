# -*-coding:utf-8-*-
from django.db import models

# Create your models here.


def dec(info):
    return info.decode('utf-8')


class Persion(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()

    def __unicode__(self):
        return self.name + str(self.age)


class Article(models.Model):
    title = models.CharField(dec('标题'), max_length=256)
    content = models.TextField(dec('内容'))
    pub_date = models.DateTimeField(dec('建立时间'), auto_now_add=True, editable=True)
    update_time = models.DateField('修改时间', auto_now=True, null=True, editable=True)

    def __unicode__(self):
        return self.title