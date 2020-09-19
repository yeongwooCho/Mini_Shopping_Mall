from django.db import models

# Create your models here.


class Order(models.Model):
    # 누가 주문한지 알기위해 (parameter는 앱안에.모델을 사용한다는 의미이다.)
    # ForeignKey를 사용할 때는 on_delete 라는 속성값을 지정해 줘야한다.
    # 사용자가 살제되면 어떻게 할 것인가, 삭제할것인가 말것인가?  삭제하도록 설정
    shopuser = models.ForeignKey(
        'shopuser.Shopuser', on_delete=models.CASCADE, verbose_name='사용자')
    product = models.ForeignKey(
        'product.Product', on_delete=models.CASCADE, verbose_name='상품')
    quantity = models.IntegerField(verbose_name='수량')
    register_date = models.DateTimeField(
        auto_now_add=True, verbose_name='주문일자')

    def __str__(self):
        return str(self.shopuser) + ' ' + str(self.product)

    class Meta:
        db_table = 'shop_order'  # 테이블명 지정
        verbose_name = '주문'
        verbose_name_plural = '주문'  # 복수형
