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
    
class ProdClass(models.Model):
    """统计每一类商品，对应四种用户行为的数量，
    存放在数据库中的商品类别信息是按照总量从大到小排序的

    Args:
        models ([type]): [description]
    """
    # products class ID
    prod_clss_id = models.CharField(max_length=20)

    # pv behavior
    pv = models.IntegerField()
    
    # buy behavior
    buy = models.IntegerField()
    
    # cart behavior
    cart = models.IntegerField()
    
    # fav behavior
    fav = models.IntegerField()

class ProdID(models.Model):
    """统计每一件商品，对应四种用户行为的数量，
    存放在数据库中的商品数量信息是按照总量从大到小排序的

    Args:
        models ([type]): [description]
    """
    # product ID
    prod_id = models.CharField(max_length=20)

    # pv behavior
    pv = models.IntegerField()
    
    # buy behavior
    buy = models.IntegerField()
    
    # cart behavior
    cart = models.IntegerField()
    
    # fav behavior
    fav = models.IntegerField()

class BuyMost(models.Model):
    """
    行为为buy的所有item中，排名前top_n个用户
    """
    # user behavior
    behavior = models.CharField(max_length=5)

    # user id
    user_id = models.CharField(max_length=10)

    # number
    number = models.IntegerField()

class FavMost(models.Model):
    """
    行为为fav的所有item中，排名前top_n个用户
    """
    # user behavior
    behavior = models.CharField(max_length=5)

    # user id
    user_id = models.CharField(max_length=10)

    # number
    number = models.IntegerField()

class CartMost(models.Model):
    """
    行为为cart的所有item中，排名前top_n个用户
    """
    # user behavior
    behavior = models.CharField(max_length=5)

    # user id
    user_id = models.CharField(max_length=10)

    # number
    number = models.IntegerField()
