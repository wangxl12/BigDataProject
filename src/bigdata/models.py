from django.db import models

# Create your models here.
class UserBehaviorTopN(models.Model):
    """创建一个数据库表，每一个元组表示一个用户，属性为
        用户ID、用户的四种行为
        每一种行为的值为统计的topn结果，使用字符串存储。

    Args:
        models ([type]): [description]
    """
    # user id
    user_id = models.CharField(max_length=7)
    
    # pv behavior
    pv = models.CharField(max_length=100)
    
    # buy behavior
    buy = models.CharField(max_length=100)
    
    # cart behavior
    cart = models.CharField(max_length=100)
    
    # fav behavior
    fav = models.CharField(max_length=100)
    