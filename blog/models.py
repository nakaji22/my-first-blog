from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    #models.ForeignKeyにはtoとondeleteの２つの引数が必要。toは関連付けるモデルを指定し、
    #on_deleteは関連付けられたオブジェクトが削除されたときの動作を指定する。
    #CASCADEは親オブジェクトが削除されたときに、関連付けられた子オブジェクトも削除されることを意味する。
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title