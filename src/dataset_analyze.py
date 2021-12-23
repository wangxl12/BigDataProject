import pandas as pd
import time
import numpy as np
from scipy.sparse import data
from tqdm.notebook import tqdm

import datetime

date_list = []
dt = datetime.datetime.strptime('2017-11-25', "%Y-%m-%d")
date = '2017-11-25'
while date <= '2017-12-03':
    date_list.append(date)
    dt = dt + datetime.timedelta(1)
    date = dt.strftime("%Y-%m-%d")

def get_unixtime(timeStr):
    formatStr = "%Y-%m-%d %H:%M:%S"
    tmObject = time.strptime(timeStr, formatStr)
    tmStamp = time.mktime(tmObject)

    return int(tmStamp)


# 数据集描述的时间范围
startTime = get_unixtime("2017-11-25 00:00:00")
endTime = get_unixtime("2017-12-3 23:59:59")
chunk_size = 100000  # chunk_size
chunks = []

df = pd.concat(chunks, ignore_index=True)
# 筛选
df_out = df.loc[(df['TimeStamps'] >= startTime) & (df['TimeStamps'] <= endTime)]

# 抽取子集
df_out = df_out.sample(frac=0.2, random_state=1)

# 去重前的数据维度
print(df.shape)  # (100150807, 5)
# 去重和抽取后的数据维度
print(df_out.shape)  # (20019035, 5)

# 输出为csv
df_out.to_csv('UserBehavior_20.csv', index=False, header=False)



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
    assert isinstance(user_id, int), "用户名输入有误!"
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10, "商品类型出错!"
    
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

def who_buys_most(df, top_n=1000):
    """行为为buy的所有item中，排名前top_n个用户

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 排名前top_n, Defaults to 1000.
    """
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10000, "top_n uncorrect!"
    # 选出行为buy的所有item
    buy_behavior = df.loc[df['行为类型'] == 'buy', : ]
    # 按照用户ID进行统计并排序，返回用户ID
    userid_num = buy_behavior['用户ID'].value_counts()[: top_n]
    user_ids = list(userid_num.keys())

    result = []
    for user_id in tqdm(user_ids):
        result.append(['buy', user_id, userid_num[user_id]])
    
    return result

def who_cart_most(df, top_n=1000):
    """行为为cart的所有item中，排名前top_n个用户

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 排名前top_n, Defaults to 1000.
    """
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10000, "top_n uncorrect!"
    # 选出行为buy的所有item
    cart_behavior = df.loc[df['行为类型'] == 'cart', : ]
    # 按照用户ID进行统计并排序，返回用户ID
    userid_num = cart_behavior['用户ID'].value_counts()[: top_n]
    user_ids = list(userid_num.keys())

    result = []
    for user_id in tqdm(user_ids):
        result.append(['cart', user_id, userid_num[user_id]])
    
    return result


def who_fav_most(df, top_n=1000):
    """行为为fav的所有item中，排名前top_n个用户

    Args:
        df (pd.DataFrame): pd.DataFrame
        top_n (int, optional): 排名前top_n, Defaults to 1000.
    """
    assert isinstance(top_n, int) and top_n > 0 and top_n < 10000, "top_n uncorrect!"
    # 选出行为buy的所有item
    fav_behavior = df.loc[df['行为类型'] == 'fav', : ]
    # 按照用户ID进行统计并排序，返回用户ID
    userid_num = fav_behavior['用户ID'].value_counts()[: top_n]
    user_ids = list(userid_num.keys())

    result = []
    for user_id in tqdm(user_ids):
        result.append(['fav', user_id, userid_num[user_id]])
    
    return result
#pv-cart-buy转化率
"""建立一个转化率字典dic_conv，其中有些项是空的，随后要填充数据进去"""
dic_conv = {
    'Step':['pv','cart','buy'],
    'Num':[],
    'Conv':[],
    'Conv_total':[]
}
"""计算每一步的数据量"""
pv_num = data[data['BehaviorType']=='pv']['UserID'].count()
cart_num = data[data['BehaviorType']=='cart']['UserID'].count()
buy_num = data[data['BehaviorType']=='buy']['UserID'].count()
"""计算转化率"""
pv2pv = round((pv_num/pv_num),4)
pv2cart = round((cart_num/pv_num),4)
cart2buy = round((buy_num/cart_num),4)
pv2buy = round((buy_num/pv_num),4)
"""更新table_conv中的每项数据'Num'列"""
dic_conv['Num'].append(pv_num)
dic_conv['Num'].append(cart_num)
dic_conv['Num'].append(buy_num)
"""更新table_conv中的每步与上一步的转化率'Conv'列"""
dic_conv['Conv'].append(pv2pv)
dic_conv['Conv'].append(pv2cart)
dic_conv['Conv'].append(cart2buy)
"""更新table_conv中的截至每步的总转化率'Conv_total'列"""
dic_conv['Conv_total'].append(pv2pv)
dic_conv['Conv_total'].append(pv2cart)
dic_conv['Conv_total'].append(pv2buy)
pd.DataFrame(dic_conv) #将结果转化为DaraFrame格式，并输出结果
#pv-fav-buy转化率
"""建立一个转化率字典dic_conv，其中有些项是空的，随后要填充数据进去"""
dic_conv = {
    'Step':['pv','fav','buy'],
    'Num':[],
    'Conv':[],
    'Conv_total':[]
}
"""计算每一步的数据量"""
pv_num = data[data['BehaviorType']=='pv']['UserID'].count()
fav_num = data[data['BehaviorType']=='fav']['UserID'].count()
buy_num = data[data['BehaviorType']=='buy']['UserID'].count()
"""计算转化率"""
pv2pv = round((pv_num/pv_num),4)
pv2fav = round((fav_num/pv_num),4)
fav2buy = round((buy_num/fav_num),4)
pv2buy = round((buy_num/pv_num),4)
"""更新table_conv中的每项数据'Num'列"""
dic_conv['Num'].append(pv_num)
dic_conv['Num'].append(fav_num)
dic_conv['Num'].append(buy_num)
"""更新table_conv中的每步与上一步的转化率'Conv'列"""
dic_conv['Conv'].append(pv2pv)
dic_conv['Conv'].append(pv2fav)
dic_conv['Conv'].append(fav2buy)
"""更新table_conv中的截至每步的总转化率'Conv_total'列"""
dic_conv['Conv_total'].append(pv2pv)
dic_conv['Conv_total'].append(pv2fav)
dic_conv['Conv_total'].append(pv2buy)
pd.DataFrame(dic_conv) #将结果转化为DaraFrame格式，并输出结果



