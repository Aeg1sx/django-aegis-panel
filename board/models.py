from django.db import models
from api_server.models import User

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField('제목', max_length=100)
    body = models.TextField('본문')
    secret = models.BooleanField('비밀 여부', default=False, null=True, blank=True)
    verify_comment = models.BooleanField('댓글 허용', default=True, null=True, blank=True)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)
    modified_at = models.DateTimeField('수정시간', auto_now=True)

    class Meta:
        ordering = ["-created_at"]


class Comment(models.Model):
    board = models.ForeignKey(Board, related_name='comments', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    parent = models.ForeignKey('self', related_name='reply', on_delete=models.CASCADE, null=True, blank=True)
    secret = models.BooleanField('비밀 여부', default=False, null=True, blank=True)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField('생성시간', auto_now_add=True)