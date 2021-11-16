import pandas as pd
import numpy as np
from tqdm.notebook import tqdm

def single_user_behavior_statistics(df, user_id, top_n=5):
    """统计单个用户行为数据

    Args:
        df (pd.DataFrame): DataFrame
        user_id (int): 用户的ID·
        top_n (int): 统计数量排名前几, 默认取前五个商品类别
    return (dict): 
        {
            user_id: {
                behavior1: [top1, top2,...,topn], 
                behavior2: [top1, top2,...,topn]
                ...
            }
        }
    """
    assert isinstance(user_id, int), "User id type uncorrect!"
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10, "top_n uncorrect!"
    
    df_tmp = df.loc[df['用户ID'] == user_id, :]
    
    df_behavior_pv = df_tmp.loc[df_tmp['行为类型'] == 'pv', :]
    df_behavior_buy = df_tmp.loc[df_tmp['行为类型'] == 'buy', :]
    df_behavior_cart = df_tmp.loc[df_tmp['行为类型'] == 'cart', :]
    df_behavior_fav = df_tmp.loc[df_tmp['行为类型'] == 'fav', :]
    
    result = dict()
    result[user_id] = dict()
    
    result[user_id]['pv'] = df_behavior_pv['商品类目ID'].value_counts()[: top_n]
    result[user_id]['buy'] = df_behavior_buy['商品类目ID'].value_counts()[: top_n]
    result[user_id]['cart'] = df_behavior_cart['商品类目ID'].value_counts()[: top_n]
    result[user_id]['fav'] = df_behavior_fav['商品类目ID'].value_counts()[: top_n]

    return result

def productsClassID_statistics(df, prod_clss=1000):
    """统计各类商品在四个行为中的数量

    Args:
        df (pd.DataFrame): DataFrame
        top_n (int, optional): 返回前n类商品. Defaults to 5.
        prod_clss (int, optional): 商品类别数量，有9439类
    return:
        [
            {prod_clss_id: [pv, buy, cart, fav]},
            {prod_clss_id: [pv, buy, cart, fav]},
            {prod_clss_id: [pv, buy, cart, fav]},
            ...
        ]
    """
    assert prod_clss > 0 and prod_clss <9440, print("商品类别数错误!")
    result = []
    prod_clss_ids = list(df['商品类目ID'].value_counts()[: prod_clss].keys())

    for prod_clss_id in tqdm(prod_clss_ids):
        # df_tmp: 商品类目ID=prod_clss_id的所有商品
        df_tmp = df.loc[df['商品类目ID'] == prod_clss_id, :]
        # 从df_tmp中选出用户行为类型为各类情况下，以行为类型统计
        bahavior_count = df_tmp['行为类型'].value_counts()

        if 'pv' not in bahavior_count:
            bahavior_count['pv'] = 0
        if 'buy' not in bahavior_count:
            bahavior_count['buy'] = 0
        if 'cart' not in bahavior_count:
            bahavior_count['cart'] = 0
        if 'fav' not in bahavior_count:
            bahavior_count['fav'] = 0
            
        result.append([prod_clss_id, [bahavior_count['pv'], 
                                      bahavior_count['buy'],
                                      bahavior_count['cart'],
                                      bahavior_count['fav']]])
    return result
        
def productsID_statisctis(df, prods=1000):
    """统计各件商品在四个行为中的排名

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 返回前n件商品. Defaults to 5.
    """
    assert prods > 0 and prods <10000, print("商品数量错误!")
    result = []
    prod_ids = list(df['商品ID'].value_counts()[: prods].keys())

    for prod_id in tqdm(prod_ids):
        # df_tmp: 商品ID=prod_id的所有商品
        df_tmp = df.loc[df['商品ID'] == prod_id, :]
        # 从df_tmp中选出用户行为类型为各类情况下，以行为类型统计
        bahavior_count = df_tmp['行为类型'].value_counts()

        if 'pv' not in bahavior_count:
            bahavior_count['pv'] = 0
        if 'buy' not in bahavior_count:
            bahavior_count['buy'] = 0
        if 'cart' not in bahavior_count:
            bahavior_count['cart'] = 0
        if 'fav' not in bahavior_count:
            bahavior_count['fav'] = 0
            
        result.append([prod_id, [bahavior_count['pv'], 
                                bahavior_count['buy'],
                                bahavior_count['cart'],
                                bahavior_count['fav']]])
    return result

def who_buys_most(df, top_n=5):
    """购买商品的用户排行

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 返回前n个购买最多的用户. Defaults to 5.
    """
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10, "top_n uncorrect!"
    user_ids = list(df['用户ID'].value_counts()[: prod_clss].keys())

def who_cart_most(df, top_n=5):
    """加入购物车的用户排行

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 返回前n个加入购物车最多的用户. Defaults to 5.
    """
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10, "top_n uncorrect!"

def who_fav_most(df, top_n=5):
    """收藏商品的用户排行

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 返回前n个收藏商品最多的用户. Defaults to 5.
    """
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10, "top_n uncorrect!"