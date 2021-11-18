import re
from django.shortcuts import render
from django.http import HttpResponse
import sqlite3
from database_op import DataBaseOP
from django.shortcuts import render, redirect, get_object_or_404
import hashlib
from itertools import chain
import json
from django.http import FileResponse
from django.shortcuts import HttpResponse
from django.http import JsonResponse
import os, sys


def index(request):
    return render(request, 'bigdata/demomap.html')
    
def buy_most_user(request):
    topn = 10
    if request.method == 'GET':
        dbop = DataBaseOP()
        dbop.select_table('bigdata_buymost')
        results = dbop.select()
        jsonData = []
        
        cnt = 0
        for tup in results:
            tmp = {}
            tmp['用户ID'] = tup[2]
            tmp['数量'] = tup[3]
            jsonData.append(tmp)
            cnt += 1
            if cnt >= topn: 
                break
        dbop.close()
    # return HttpResponse(jsonData)
    return JsonResponse(jsonData, json_dumps_params={'ensure_ascii': False}, safe=False)

def cart_most_user(request):
    topn = 10
    if request.method == 'GET':
        dbop = DataBaseOP()
        dbop.select_table('bigdata_cartmost')
        results = dbop.select()
        jsonData = []
        
        cnt = 0
        for tup in results:
            tmp = {}
            tmp['用户ID'] = tup[2]
            tmp['数量'] = tup[3]
            jsonData.append(tmp)
            cnt += 1
            if cnt >= topn: 
                break
        dbop.close()
    # return HttpResponse(jsonData)
    return JsonResponse(jsonData, json_dumps_params={'ensure_ascii': False}, safe=False)

def fav_most_user(request):
    topn = 40
    if request.method == 'GET':
        dbop = DataBaseOP()
        dbop.select_table('bigdata_favmost')
        results = dbop.select()
        jsonData = []
        
        cnt = 0
        for tup in results:
            tmp = {}
            tmp['用户ID'] = tup[2]
            tmp['数量'] = tup[3]
            jsonData.append(tmp)
            cnt += 1
            if cnt >= topn: 
                break
        dbop.close()
    # return HttpResponse(jsonData)
    return JsonResponse(jsonData, json_dumps_params={'ensure_ascii': False}, safe=False)

def productsID_statisctis(request):
    topn = 5
    if request.method == 'GET':
        dbop = DataBaseOP()
        dbop.select_table('bigdata_prodid')
        results = dbop.select()
        jsonData = []
        
        cnt = 0
        for tup in results:
            tmp = {}
            tmp['prod_id'] = tup[1]
            tmp['pv'] = tup[2]
            tmp['buy'] = tup[3]
            tmp['cart'] = tup[4]
            tmp['fav'] = tup[5]
            jsonData.append(tmp)
            cnt += 1
            if cnt >= topn: 
                break
        dbop.close()
    # return HttpResponse(jsonData)
    return JsonResponse(jsonData, json_dumps_params={'ensure_ascii': False}, safe=False)

def productsClassID_statistics(request):
    topn = 35
    if request.method == 'GET':
        dbop = DataBaseOP()
        dbop.select_table('bigdata_prodclass')
        results = dbop.select()
        jsonData = []
        
        cnt = 0
        for tup in results:
            tmp = {}
            tmp['prodclss_id'] = tup[1]
            tmp['pv'] = tup[2]
            tmp['buy'] = tup[3]
            tmp['cart'] = tup[4]
            tmp['fav'] = tup[5]
            jsonData.append(tmp)
            cnt += 1
            if cnt >= topn: 
                break
        dbop.close()
    # return HttpResponse(jsonData)
    return JsonResponse(jsonData, json_dumps_params={'ensure_ascii': False}, safe=False)

def single_user_behavior_statistics(request):
    topn = 60
    if request.method == 'GET':
        dbop = DataBaseOP()
        dbop.select_table('bigdata_userbehaviortopn')
        results = dbop.select()
        jsonData = []
        
        cnt = 0
        for tup in results:
            tmp = {}
            tmp['user_id'] = tup[1]
            if tup[2] == '0':
                tmp['pv'] = 0
            else:
                tmp['pv'] = int(tup[2].split('\t')[0].split(' ')[1].split(')')[0])
            if tup[3] == '0':
                tmp['buy'] = 0
            else:
                tmp['buy'] = int(tup[3].split('\t')[0].split(' ')[1].split(')')[0])
            if tup[4] == '0':
                tmp['cart'] = 0
            else:
                tmp['cart'] = int(tup[4].split('\t')[0].split(' ')[1].split(')')[0])
            if tup[5] == '0':
                tmp['fav'] = 0
            else:
                tmp['fav'] = int(tup[5].split('\t')[0].split(' ')[1].split(')')[0])
            
            jsonData.append(tmp)
            cnt += 1
            if cnt >= topn: 
                break
        dbop.close()
    # return HttpResponse(jsonData)
    return JsonResponse(jsonData, json_dumps_params={'ensure_ascii': False}, safe=False)