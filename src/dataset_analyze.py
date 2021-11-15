import pandas as pd
import numpy as np

def single_user_behavior_statistics(user_id, top_n=5):
    """统计单个用户行为数据

    Args:
        user_id (int): 用户的ID·
        top_n (int): 统计数量排名前几, 默认取前五个
    return (dict): 
        {user_id: {behavior1: [top1, top2,...,topn], behavior2: [top1, top2,...,topn]}} 
    """
    assert isinstance(user_id, int), "User id type uncorrect!"
    assert isinstance(top_n, int) and top_n > 0 and top_n < 1000000, "top_n uncorrect!"
    
    
    
    