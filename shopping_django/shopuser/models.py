from django.db import models

# Create your models here.


class Shopuser(models.Model):
    # 관리자 페이지에서 유용하게 사용하도록 verbose_name지정
    objects = models.Manager()
    email = models.EmailField(verbose_name='이메일')
    password = models.CharField(max_length=64, verbose_name='비밀번호')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='등록날짜')

    def __str__(self):
        return self.email

    class Meta:
        db_table = 'shop_user'  # 테이블명 지정
        verbose_name = '사용자'
        verbose_name_plural = '사용자'  # 복수형
